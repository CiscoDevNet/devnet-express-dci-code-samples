## More Powerful Cisco Compute Python Scripts with UCS Python SDK
## Exercise 1

from ucsmsdk.ucscoreutils import get_meta_info

meta = get_meta_info(class_id="FabricVlan")
print(meta)

vars(meta)

meta.class_id; meta.xml_attribute; meta.rn; meta.min_version; meta.access_privilege; meta.parents; meta.children

vars(meta.min_version)

meta.class_id; meta.xml_attribute; meta.rn; meta.min_version._UcsVersion__version; meta.access_privilege; meta.parents; meta.children

meta.props

meta.props["id"]
meta.props["name"]

vars(meta.props["id"].restriction)
vars(meta.props["name"].restriction)


for vlan_property in meta.props:
    print("ATTRIBUTE NAME: " + vlan_property)
    print("    PATTERN:   " + str(meta.props[vlan_property].restriction.pattern))
    print("    VALUE_SET: " + str(meta.props[vlan_property].restriction.value_set))
    print("    RANGE_VAL: " + str(meta.props[vlan_property].restriction.range_val))

meta.props["name"].restriction.pattern
meta.props["id"].restriction.range_val
