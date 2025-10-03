import json
from pythonosc import osc_message_builder
from helper import resource_path


class OSCConfig:
    """Load and manage OSC configuration from JSON file"""

    def __init__(self, config_path=None):
        if config_path is None:
            config_path = resource_path("qlab_osc_config.json")

        with open(config_path, 'r') as f:
            self.config = json.load(f)

        self.global_properties = self.config.get('global_properties', {})
        self.cue_type_properties = self.config.get('cue_type_properties', {})
        self.valid_cue_types = self.config.get('valid_cue_types', [])

    def get_valid_cue_types(self):
        """Return list of valid cue types"""
        return self.valid_cue_types

    def check_cue_type(self, cue_type):
        """Return the valid type of cue, or False"""
        cue_type = cue_type.lower()
        if cue_type not in self.valid_cue_types:
            return False
        return cue_type

    def get_property_config(self, property_name, cue_type=None, qlab_version=None):
        """
        Get configuration for a specific property

        Args:
            property_name: The CSV column name (normalized to lowercase, no spaces)
            cue_type: Optional cue type for cue-specific properties
            qlab_version: Optional QLab version (4 or 5) for version-specific properties

        Returns:
            Property configuration dict or None if not found
        """
        property_name = property_name.lower()

        # Check global properties first
        if property_name in self.global_properties:
            return self.global_properties[property_name]

        # Check cue-type-specific properties
        if cue_type:
            cue_type = cue_type.lower()

            # Handle network cues with version-specific properties
            if cue_type == 'network' and qlab_version:
                qlab_key = f'qlab{qlab_version}'
                if qlab_key in self.cue_type_properties.get('network', {}):
                    network_props = self.cue_type_properties['network'][qlab_key]
                    if property_name in network_props:
                        return network_props[property_name]

            # Check other cue-type properties
            if cue_type in self.cue_type_properties:
                if property_name in self.cue_type_properties[cue_type]:
                    return self.cue_type_properties[cue_type][property_name]

        return None

    def build_osc_message(self, property_name, value, cue_type=None, qlab_version=None, cue_data=None):
        """
        Build an OSC message for a property

        Args:
            property_name: The property name (CSV column header)
            value: The value to set
            cue_type: Optional cue type for cue-specific properties
            qlab_version: Optional QLab version for version-specific properties
            cue_data: Optional full cue data dict for conditional properties

        Returns:
            OscMessageBuilder or None if property not found
        """
        if not value:
            return None

        prop_config = self.get_property_config(property_name, cue_type, qlab_version)

        if not prop_config:
            return None

        # Check conditions if present
        if 'condition' in prop_config and cue_data:
            condition = prop_config['condition']
            condition_field = condition.get('field')
            condition_value = condition.get('value')

            if cue_data.get(condition_field) != condition_value:
                return None

        # Validate value if validation rules exist
        if 'valid_range' in prop_config:
            try:
                int_value = int(value)
                min_val, max_val = prop_config['valid_range']
                if int_value < min_val or int_value > max_val:
                    return None
            except ValueError:
                return None

        if 'valid_values' in prop_config:
            if value.lower() not in [v.lower() for v in prop_config['valid_values']]:
                return None

        # Build the message
        msg = osc_message_builder.OscMessageBuilder(address=prop_config['osc_address'])

        # Add argument based on type
        value_type = prop_config.get('type', 'string')

        try:
            if value_type == 'int':
                msg.add_arg(int(value))
            elif value_type == 'float':
                msg.add_arg(float(value))
            elif value_type == 'bool':
                # Handle various boolean representations
                bool_value = value.lower() in ['true', '1', 'yes', 'on'] if isinstance(value, str) else bool(value)
                msg.add_arg(bool_value)
            else:  # string
                msg.add_arg(str(value))
        except (ValueError, AttributeError):
            return None

        return msg

    def get_auto_properties(self, property_name, cue_type=None):
        """
        Get properties that should be automatically set when a property is set

        For example, when fadeopacity is set, doopacity should also be set to true

        Returns:
            List of (property_name, value) tuples
        """
        auto_props = []

        if cue_type and cue_type in self.cue_type_properties:
            cue_props = self.cue_type_properties[cue_type]

            # Check if this property has any related auto properties
            for prop_key, prop_config in cue_props.items():
                if 'auto_value' in prop_config and prop_key != property_name:
                    # Check if this auto property is related to the current property
                    # For now, we'll handle the specific case of fadeopacity -> doopacity
                    if property_name == 'fadeopacity' and prop_key == 'doopacity':
                        auto_props.append((prop_key, prop_config['auto_value']))

        return auto_props


# Singleton instance
_osc_config_instance = None

def get_osc_config():
    """Get or create the singleton OSC config instance"""
    global _osc_config_instance
    if _osc_config_instance is None:
        _osc_config_instance = OSCConfig()
    return _osc_config_instance
