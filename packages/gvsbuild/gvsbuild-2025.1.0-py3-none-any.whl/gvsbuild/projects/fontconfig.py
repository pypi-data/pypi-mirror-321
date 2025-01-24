#  Copyright (C) 2016 The Gvsbuild Authors
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, see <http://www.gnu.org/licenses/>.

from gvsbuild.utils.base_builders import Meson
from gvsbuild.utils.base_expanders import Tarball
from gvsbuild.utils.base_project import Project, project_add


@project_add
class Fontconfig(Tarball, Meson):
    def __init__(self):
        Project.__init__(
            self,
            "fontconfig",
            version="2.15.0",
            lastversion_even=True,
            repository="https://gitlab.freedesktop.org/fontconfig/fontconfig",
            archive_url="https://www.freedesktop.org/software/fontconfig/release/fontconfig-{version}.tar.gz",
            hash="f5f359d6332861bd497570848fcb42520964a9e83d5e3abe397b6b6db9bcaaf4",
            dependencies=["freetype", "gperf", "expat"],
        )
        self.add_param("-Dtests=disabled")

    def build(self):
        Meson.build(self)
        self.install(r".\COPYING share\doc\fontconfig")
