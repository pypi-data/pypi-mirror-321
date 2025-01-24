from typing import Any, Dict

from setuptools import Extension
from setuptools.command.build_ext import build_ext
from setuptools.errors import CompileError

extension = Extension(
    name="fair_kmeans._core",
    sources=[
        "fair_kmeans/_core.cpp",
        "fair_kmeans/fair_clustering_tools.cpp",
        "fair_kmeans/point.cpp",
    ],
    include_dirs=["fair_kmeans"],
)

# Thank you https://github.com/dstein64/kmeans1d!


class BuildExt(build_ext):
    """A custom build extension for adding -stdlib arguments for clang++."""

    def build_extensions(self) -> None:
        # '-std=c++11' is added to `extra_compile_args` so the code can compile
        # with clang++. This works across compilers (ignored by MSVC).
        for extension in self.extensions:
            extension.extra_compile_args.append("-std=c++11")
            extension.extra_compile_args.append("-DLEMON_ONLY_TEMPLATES")

        try:
            build_ext.build_extensions(self)
        except CompileError:
            # Workaround Issue #2.
            # '-stdlib=libc++' is added to `extra_compile_args` and `extra_link_args`
            # so the code can compile on macOS with Anaconda.
            for extension in self.extensions:
                extension.extra_compile_args.append("-stdlib=libc++")
                extension.extra_compile_args.append("-DLEMON_ONLY_TEMPLATES")
                extension.extra_link_args.append("-stdlib=libc++")
            build_ext.build_extensions(self)


def build(setup_kwargs: Dict[str, Any]) -> None:
    setup_kwargs.update(
        {"ext_modules": [extension], "cmdclass": {"build_ext": BuildExt}}
    )
