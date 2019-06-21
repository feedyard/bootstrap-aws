"""invoke tasks for the feedyard/bootstrap-aws resource"""
from invoke import Collection
from tasks import deploy
from tasks import delete
from tasks import idp

ns = Collection()
ns.add_collection(deploy)
ns.add_collection(delete)
ns.add_collection(idp)