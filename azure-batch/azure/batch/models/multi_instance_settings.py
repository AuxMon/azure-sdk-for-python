# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MultiInstanceSettings(Model):
    """Settings which specify how to run a multi-instance task.

    Multi-instance tasks are commonly used to support MPI tasks.

    :param number_of_instances: The number of compute nodes required by the
     task.
    :type number_of_instances: int
    :param coordination_command_line: The command line to run on all the
     compute nodes to enable them to coordinate when the primary runs the main
     task command. A typical coordination command line launches a background
     service and verifies that the service is ready to process inter-node
     messages.
    :type coordination_command_line: str
    :param common_resource_files: A list of files that the Batch service will
     download before running the coordination command line. The difference
     between common resource files and task resource files is that common
     resource files are downloaded for all subtasks including the primary,
     whereas task resource files are downloaded only for the primary.
    :type common_resource_files: list of :class:`ResourceFile
     <azure.batch.models.ResourceFile>`
    """

    _validation = {
        'number_of_instances': {'required': True},
    }

    _attribute_map = {
        'number_of_instances': {'key': 'numberOfInstances', 'type': 'int'},
        'coordination_command_line': {'key': 'coordinationCommandLine', 'type': 'str'},
        'common_resource_files': {'key': 'commonResourceFiles', 'type': '[ResourceFile]'},
    }

    def __init__(self, number_of_instances, coordination_command_line=None, common_resource_files=None):
        self.number_of_instances = number_of_instances
        self.coordination_command_line = coordination_command_line
        self.common_resource_files = common_resource_files
