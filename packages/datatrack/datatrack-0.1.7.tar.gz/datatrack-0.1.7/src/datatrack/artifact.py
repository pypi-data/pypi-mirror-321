# datatrack: tracks your data transformations.
# Copyright (C) 2024  Roman Kindruk

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


import getpass
import logging
from pathlib import Path

from datatrack import dbaccess as db
from datatrack.config import config
from datatrack.s3path import S3Path


class Artifact:
    def __init__(self, id):
        self._id = id

    @property
    def id(self):
        return self._id

    @staticmethod
    def _make_path(project, artifact_id):
        return str(Path(project) / "artifacts" / artifact_id)

    @staticmethod
    def _make_s3path(project, artifact_id):
        return S3Path(
            config()["s3"]["bucket"], config()["s3"]["prefix"]
        ) / Artifact._make_path(project, artifact_id)

    def download(self, dst=None):
        logger = logging.getLogger(__name__)
        a = db.get_artifact(self._id)
        if a is None:
            raise RuntimeError(f"{self} is not found")
        loc = self._make_s3path(a["project"], self._id)
        if dst is None:
            dst = Path(config()["cache"]) / self._make_path(a["project"], self._id)
            if dst.exists():
                logger.info(f"{self} is found in {dst}")
                return dst
        loc.download(dst)
        return dst

    @staticmethod
    def create(project, name, src, pattern="**/*"):
        aid = db.create_artifact(project, name, getpass.getuser())
        dst = Artifact._make_s3path(project, aid)
        if isinstance(src, str) and src.startswith("s3://"):
            dst.copy_from(S3Path.from_uri(src))
        else:
            dst.upload(src, pattern)
        db.add_artifact_objects(aid, dst.rglob("*"))
        return Artifact(aid)

    def __repr__(self):
        return f"Artifact(id='{self._id}')"
