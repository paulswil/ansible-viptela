#!/usr/bin/env python

ANSIBLE_METADATA = {
    'metadata_version': '1.1',
    'status': ['preview'],
    'supported_by': 'community'
}

import requests
from ansible.module_utils.basic import AnsibleModule, json
from ansible.module_utils.viptela import viptelaModule, viptela_argument_spec


def run_module():
    # define available arguments/parameters a user can pass to the module
    argument_spec = viptela_argument_spec()
    argument_spec.update(factory_default=dict(type='bool', default=False),
                         )

    # seed the result dict in the object
    # we primarily care about changed and state
    # change is if this module effectively modified the target
    # state will include any data that you want your module to pass back
    # for consumption, for example, in a subsequent task
    result = dict(
        changed=False,
        original_message='',
        message=''
    )

    # the AnsibleModule object will be our abstraction working with Ansible
    # this includes instantiation, a couple of common attr would be the
    # args/params passed to the execution, as well as if the module
    # supports check mode
    module = AnsibleModule(argument_spec=argument_spec,
                           supports_check_mode=True,
                           )
    viptela = viptelaModule(module)

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    if module.check_mode:
        return result

    viptela.result['feature_templates'] = viptela.get_feature_templates(factory_default=viptela.params['factory_default'])
    viptela.result['device_templates'] = viptela.get_device_templates(factory_default=viptela.params['factory_default'])

    # if the user is working with this module in only check mode we do not
    # want to make any changes to the environment, just return the current
    # state with no modifications
    # FIXME: Work with viptela so they can implement a check mode
    if module.check_mode:
        viptela.exit_json(**viptela.result)

    # execute checks for argument completeness

    # manipulate or modify the state as needed (this is going to be the
    # part where your module will do what it needs to do)

    # in the event of a successful module execution, you will want to
    # simple AnsibleModule.exit_json(), passing the key/value results
    viptela.exit_json(**viptela.result)

def main():
    run_module()

if __name__ == '__main__':
    main()