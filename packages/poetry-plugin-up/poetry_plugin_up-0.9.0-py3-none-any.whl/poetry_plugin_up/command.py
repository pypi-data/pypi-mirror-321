from typing import Any, Dict, Iterable, List

from cleo.helpers import argument, option
from packaging.version import parse as parse_version
from poetry.__version__ import __version__ as poetry_version
from poetry.console.commands.installer_command import InstallerCommand
from poetry.core.constraints.version import parse_constraint
from poetry.core.packages.dependency import Dependency
from poetry.core.packages.dependency_group import DependencyGroup
from poetry.core.packages.package import Package
from poetry.version.version_selector import VersionSelector
from tomlkit import array, dumps, table
from tomlkit.toml_document import TOMLDocument


class UpCommand(InstallerCommand):
    name = "up"
    description = (
        "Update dependencies and bump versions in <comment>pyproject.toml</>"
    )

    arguments = [
        argument(
            name="packages",
            description="The packages to update.",
            optional=True,
            multiple=True,
        )
    ]

    options = [
        *InstallerCommand._group_dependency_options(),
        option(
            long_name="latest",
            short_name=None,
            description="Update to latest available compatible versions.",
        ),
        option(
            long_name="pinned",
            short_name=None,
            description=(
                "Include pinned (exact) dependencies when updating to latest."
            ),
        ),
        option(
            long_name="exclude",
            short_name=None,
            description="Exclude dependencies.",
            multiple=True,
            flag=False,
        ),
        option(
            long_name="no-install",
            short_name=None,
            description="Do not install dependencies, only refresh "
            "<comment>pyproject.toml</> and <comment>poetry.lock</>.",
        ),
        option(
            long_name="dry-run",
            short_name=None,
            description="Output bumped <comment>pyproject.toml</> but do not "
            "execute anything.",
        ),
        option(
            long_name="exclude-zero-based-caret",
            short_name=None,
            description="Exclude zero-based caret dependencies "
            "when updating to latest.",
        ),
        option(
            long_name="preserve-wildcard",
            short_name=None,
            description="Do not bump wildcard dependencies "
            "when updating to latest.",
        ),
    ]

    def handle(self) -> int:
        only_packages = self.argument("packages")
        latest = self.option("latest")
        pinned = self.option("pinned")
        no_install = self.option("no-install")
        dry_run = self.option("dry-run")
        exclude = self.option("exclude")
        exclude_zero_based_caret = self.option("exclude-zero-based-caret")
        preserve_wildcard = self.option("preserve-wildcard")

        if pinned and not latest:
            self.line_error("'--pinned' specified without '--latest'")
            raise Exception

        if exclude_zero_based_caret and not latest:
            self.line_error(
                "'--exclude-zero-based-caret' specified without '--latest'"
            )
            raise Exception

        if preserve_wildcard and not latest:
            self.line_error(
                "'--preserve-wildcard' specified without '--latest'"
            )
            raise Exception

        selector = VersionSelector(self.poetry.pool)
        pyproject_content = self.poetry.file.read()
        original_pyproject_content = self.poetry.file.read()

        for dependency in self.get_dependencies():
            self.handle_dependency(
                dependency=dependency,
                latest=latest,
                pinned=pinned,
                only_packages=only_packages,
                pyproject_content=pyproject_content,
                selector=selector,
                exclude=exclude,
                exclude_zero_based_caret=exclude_zero_based_caret,
                preserve_wildcard=preserve_wildcard,
            )

        if dry_run:
            self.line(dumps(pyproject_content))
            return 0

        # write new content to pyproject.toml
        self.poetry.file.write(pyproject_content)
        self.reset_poetry()

        try:
            if no_install:
                # update lock file
                if poetry_version_above_2():
                    self.call(name="lock", args="--regenerate")
                else:
                    self.call(name="lock")
            else:
                # update dependencies
                self.call(name="update")
        except Exception as e:
            self.line("\nReverting <comment>pyproject.toml</>")
            self.poetry.file.write(original_pyproject_content)
            raise e
        return 0

    def get_dependencies(self) -> Iterable[DependencyGroup]:
        """Returns activated dependency groups"""
        for group in self.activated_groups:
            yield from self.poetry.package.dependency_group(group).dependencies

    def handle_dependency(
        self,
        dependency: Dependency,
        latest: bool,
        pinned: bool,
        only_packages: List[str],
        pyproject_content: TOMLDocument,
        selector: VersionSelector,
        exclude: List[str],
        exclude_zero_based_caret: bool,
        preserve_wildcard: bool,
    ) -> None:
        """Handles a dependency"""
        if not self.is_bumpable(
            dependency,
            only_packages,
            latest,
            pinned,
            exclude,
            exclude_zero_based_caret,
            preserve_wildcard,
        ):
            return

        target_package_version = dependency.pretty_constraint
        if latest:
            target_package_version = "*"

        candidate: Package = selector.find_best_candidate(
            package_name=dependency.name,
            target_package_version=target_package_version,
            allow_prereleases=dependency.allows_prereleases(),
            source=dependency.source_name,
        )
        if candidate is None:
            self.line(f"No new version for '{dependency.name}'")
            return

        if (
            dependency.pretty_constraint[0] == "~"
            and "." in dependency.pretty_constraint
        ):
            new_version = "~" + candidate.pretty_version
        elif (
            dependency.pretty_constraint[:2] == ">="
            and len(dependency.pretty_constraint.split(",")) == 1
        ):
            new_version = ">=" + candidate.pretty_version
        else:
            new_version = "^" + candidate.pretty_version

        self.bump_version_in_pyproject_content(
            dependency=dependency,
            new_version=new_version,
            pyproject_content=pyproject_content,
        )

    @staticmethod
    def is_bumpable(
        dependency: Dependency,
        only_packages: List[str],
        latest: bool,
        pinned: bool,
        exclude: List[str],
        exclude_zero_based_caret: bool,
        preserve_wildcard: bool,
    ) -> bool:
        """Determines if a dependency can be bumped in pyproject.toml"""
        if dependency.source_type in ["git", "file", "directory"]:
            return False
        if dependency.name in ["python"]:
            return False
        if only_packages and dependency.name not in only_packages:
            return False
        if dependency.name in exclude:
            return False
        if (
            exclude_zero_based_caret
            and dependency.pretty_constraint.startswith("^0")
        ):
            return False

        constraint = dependency.pretty_constraint
        if preserve_wildcard and constraint == "*":
            return False

        if not latest:
            if is_pinned(constraint):
                # pinned
                return False
            if constraint[0] == "*":
                # wildcard
                return False
            if constraint[0] == "<" and constraint[1].isdigit():
                # less than
                return False
            if constraint[0] == ">" and constraint[1].isdigit():
                # greater than
                return False
            if constraint[:2] == "<=":
                # less than or equal to
                return False
            if constraint[:2] == "!=":
                # inequality
                return False
            if len(constraint.split(",")) > 1:
                # multiple requirements e.g. '>=1.0.0, <2.0.0'
                return False

        if not pinned:
            if is_pinned(constraint):
                # pinned
                return False

        return True

    @staticmethod
    def bump_version_in_pyproject_content(
        dependency: Dependency,
        new_version: str,
        pyproject_content: TOMLDocument,
    ) -> None:
        """Bumps versions in pyproject content (pyproject.toml)"""
        project_content = pyproject_content.get("project", table())
        if uses_pep508_style(pyproject_content):
            for group in dependency.groups:
                sections = []
                if group == "main":
                    sections.append(
                        project_content.get("dependencies", array())
                    )
                    opt_deps = project_content.get("optional-dependencies", {})
                    for section in opt_deps.values():
                        sections.append(section)
                elif group in (
                    dep_groups := pyproject_content.get("dependency-groups", {})
                ):
                    sections.append(dep_groups.get(group, array()))
                for section in sections:
                    for index, entry in enumerate(section):
                        entry_dependency = Dependency.create_from_pep_508(entry)
                        if (
                            entry_dependency.name == dependency.name
                            and entry_dependency.constraint
                            != parse_constraint(new_version)
                        ):
                            entry_dependency.constraint = new_version
                            section[index] = entry_dependency.to_pep_508()

        poetry_content: Dict[str, Any] = pyproject_content.get("tool", {}).get(
            "poetry", {}
        )

        for group in dependency.groups:
            # find section to modify
            section = {}
            if group == "main":
                section = poetry_content.get("dependencies", {})
            elif group == "dev" and "dev-dependencies" in poetry_content:
                # take account for the old `dev-dependencies` section
                section = poetry_content.get("dev-dependencies", {})
            else:
                section = (
                    poetry_content.get("group", {})
                    .get(group, {})
                    .get("dependencies", {})
                )

            # modify section
            if isinstance(section.get(dependency.pretty_name), str):
                section[dependency.pretty_name] = new_version
            elif "version" in section.get(dependency.pretty_name, {}):
                section[dependency.pretty_name]["version"] = new_version


def is_pinned(version: str) -> bool:
    """Returns if `version` is an exact version."""
    return version[0].isdigit() or version[:2] == "=="


def uses_pep508_style(pyproject_content: TOMLDocument) -> bool:
    project_content = pyproject_content.get("project", table())
    return (
        "dependencies" in project_content
        or "optional-dependencies" in project_content
        or "dependency-groups" in pyproject_content
    )


def poetry_version_above_2() -> bool:
    return parse_version(poetry_version) >= parse_version("2.0.0")
