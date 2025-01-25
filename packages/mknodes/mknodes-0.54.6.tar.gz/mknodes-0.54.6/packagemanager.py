"""Module for handling Python distribution and package information."""

from __future__ import annotations

import dataclasses
from importlib import metadata
from typing import TYPE_CHECKING, TypeVar

import upath


if TYPE_CHECKING:
    from collections.abc import Callable, Iterator
    import email.message

T = TypeVar("T")


@dataclasses.dataclass(frozen=True)
class PackageInfo:
    """Container for package information including all metadata fields."""

    # Basic package information
    name: str
    version: str | None = None
    location: str | None = None
    files: list[str] | None = None
    requires: list[str] | None = None
    entry_points: dict[str, list[str]] | None = None

    # Standard metadata fields
    metadata_version: str | None = None
    summary: str | None = None
    home_page: str | None = None
    author: str | None = None
    author_email: str | None = None
    license: str | None = None
    description: str | None = None
    keywords: list[str] | None = None
    platform: list[str] | None = None
    classifiers: list[str] | None = None
    download_url: str | None = None
    requires_dist: list[str] | None = None
    requires_python: str | None = None
    provides_dist: list[str] | None = None
    obsoletes_dist: list[str] | None = None
    requires_external: list[str] | None = None
    project_urls: dict[str, str] | None = None
    maintainer: str | None = None
    maintainer_email: str | None = None
    description_content_type: str | None = None
    long_description: str | None = None
    long_description_content_type: str | None = None
    provides_extra: list[str] | None = None


class DistributionManager:
    """Manages distribution and package information with caching."""

    def __init__(self) -> None:
        """Initialize the distribution manager."""
        self._cache: dict[str, PackageInfo] = {}
        self._dist_cache: dict[str, metadata.Distribution] = {}

    def _get_distribution(self, name: str) -> metadata.Distribution:
        """Get distribution with caching."""
        if name not in self._dist_cache:
            try:
                self._dist_cache[name] = metadata.distribution(name)
            except metadata.PackageNotFoundError as exc:
                msg = f"Distribution {name!r} not found"
                raise ValueError(msg) from exc
        return self._dist_cache[name]

    @staticmethod
    def _parse_list_field(value: str | None) -> list[str] | None:
        """Parse comma-separated fields into list."""
        if not value:
            return None
        return [item.strip() for item in value.split(",") if item.strip()]

    @staticmethod
    def _parse_project_urls(metadata_obj: email.message.Message) -> dict[str, str]:
        """Parse project URLs from metadata."""
        urls: dict[str, str] = {}
        for key in metadata_obj:
            if key.lower().startswith("project-url"):
                name = key.split(":")[-1].strip()
                if url := metadata_obj[key]:
                    urls[name] = url
        return urls or None

    def _cache_package_info(self, name: str) -> None:
        """Cache package information."""
        if name in self._cache:
            return

        dist = self._get_distribution(name)
        metadata_obj = dist.metadata
        entry_points = self._group_entry_points(dist)

        self._cache[name] = PackageInfo(
            # Basic package information
            name=dist.name,
            version=dist.version,
            location=str(dist.locate_file("")) if dist._path else None,
            files=[str(f) for f in dist.files or []],
            requires=[str(r) for r in dist.requires or []],
            entry_points=entry_points,
            # Standard metadata fields
            metadata_version=metadata_obj.get("Metadata-Version"),
            summary=metadata_obj.get("Summary"),
            home_page=metadata_obj.get("Home-page"),
            author=metadata_obj.get("Author"),
            author_email=metadata_obj.get("Author-email"),
            license=metadata_obj.get("License"),
            description=metadata_obj.get("Description"),
            keywords=self._parse_list_field(metadata_obj.get("Keywords")),
            platform=self._parse_list_field(metadata_obj.get("Platform")),
            classifiers=self._parse_list_field(metadata_obj.get("Classifier")),
            download_url=metadata_obj.get("Download-URL"),
            requires_dist=self._parse_list_field(metadata_obj.get("Requires-Dist")),
            requires_python=metadata_obj.get("Requires-Python"),
            provides_dist=self._parse_list_field(metadata_obj.get("Provides-Dist")),
            obsoletes_dist=self._parse_list_field(metadata_obj.get("Obsoletes-Dist")),
            requires_external=self._parse_list_field(
                metadata_obj.get("Requires-External")
            ),
            project_urls=self._parse_project_urls(metadata_obj),
            maintainer=metadata_obj.get("Maintainer"),
            maintainer_email=metadata_obj.get("Maintainer-email"),
            description_content_type=metadata_obj.get("Description-Content-Type"),
            long_description=metadata_obj.get("Long-Description"),
            long_description_content_type=metadata_obj.get(
                "Long-Description-Content-Type"
            ),
            provides_extra=self._parse_list_field(metadata_obj.get("Provides-Extra")),
        )

    @staticmethod
    def _group_entry_points(
        dist: metadata.Distribution,
    ) -> dict[str, list[str]]:
        """Group entry points by group name."""
        result: dict[str, list[str]] = {}
        for ep in dist.entry_points:
            result.setdefault(ep.group, []).append(str(ep))
        return result

    def get_package_info(self, name: str) -> PackageInfo:
        """Get complete package information."""
        self._cache_package_info(name)
        return self._cache[name]

    def get_package_location(
        self, name: str, *, as_string: bool = False
    ) -> upath.UPath | str | None:
        """Get the package location.

        Args:
            name: Package name
            as_string: If True, return string instead of UPath

        Returns:
            Package location as UPath or string, None if not found
        """
        self._cache_package_info(name)
        if location := self._cache[name].location:
            return location if as_string else upath.UPath(location)
        return None

    def get_package_files(self, name: str) -> list[str]:
        """Get list of package files."""
        return self.get_package_info(name).files or []

    def get_package_requires(self, name: str) -> list[str]:
        """Get package requirements."""
        return self.get_package_info(name).requires or []

    def get_entry_points(self, name: str) -> dict[str, list[str]]:
        """Get package entry points grouped by type."""
        return self.get_package_info(name).entry_points or {}

    def get_version(self, name: str) -> str | None:
        """Get package version."""
        return self.get_package_info(name).version

    def iter_distributions(self) -> Iterator[str]:
        """Iterate over all installed distributions."""
        yield from metadata.distributions()

    def find_packages(self, predicate: Callable[[str], bool]) -> list[str]:
        """Find packages matching the predicate."""
        return [dist for dist in self.iter_distributions() if predicate(dist)]

    def get_main_package(self, name: str) -> str:
        """Get the main package name (without underscore prefix).

        Args:
            name: Distribution name

        Returns:
            Main package name

        Raises:
            ValueError: If no Python modules found in distribution
        """
        dist = self._get_distribution(name)

        # Look for non-underscore prefixed modules first
        for file in dist.files or []:
            if file.name.endswith(".py"):
                module_name = file.name[:-3]
                if not module_name.startswith("_"):
                    return module_name

        # If no main package found, return the first module
        for file in dist.files or []:
            if file.name.endswith(".py"):
                return file.name[:-3]

        msg = f"No Python modules found in distribution {name!r}"
        raise ValueError(msg)


if __name__ == "__main__":
    manager = DistributionManager()
    info = manager.get_package_info("requests")
    print(f"Package: {info.name} {info.version}")
    print(f"Author: {info.author} <{info.author_email}>")
    print(f"Description: {info.summary}")
    print(f"Homepage: {info.home_page}")
    print(f"Requires Python: {info.requires_python}")
    print("Project URLs:")
    for name, url in (info.project_urls or {}).items():
        print(f"  {name}: {url}")
