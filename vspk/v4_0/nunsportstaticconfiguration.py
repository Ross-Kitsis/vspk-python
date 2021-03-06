# -*- coding: utf-8 -*-
#
# Copyright (c) 2015, Alcatel-Lucent Inc
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its contributors
#       may be used to endorse or promote products derived from this software without
#       specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.



from .fetchers import NUMetadatasFetcher


from .fetchers import NUGlobalMetadatasFetcher

from bambou import NURESTObject


class NUNSPortStaticConfiguration(NURESTObject):
    """ Represents a NSPortStaticConfiguration in the VSD

        Notes:
            Represents a network port static configuration in the context of an Network Services Gateway.
    """

    __rest_name__ = "nsportstaticconfiguration"
    __resource_name__ = "nsportstaticconfigurations"

    
    ## Constants
    
    CONST_ENTITY_SCOPE_GLOBAL = "GLOBAL"
    
    CONST_ENTITY_SCOPE_ENTERPRISE = "ENTERPRISE"
    
    

    def __init__(self, **kwargs):
        """ Initializes a NSPortStaticConfiguration instance

            Notes:
                You can specify all parameters while calling this methods.
                A special argument named `data` will enable you to load the
                object from a Python dictionary

            Examples:
                >>> nsportstaticconfiguration = NUNSPortStaticConfiguration(id=u'xxxx-xxx-xxx-xxx', name=u'NSPortStaticConfiguration')
                >>> nsportstaticconfiguration = NUNSPortStaticConfiguration(data=my_dict)
        """

        super(NUNSPortStaticConfiguration, self).__init__()

        # Read/Write Attributes
        
        self._dns_address = None
        self._last_updated_by = None
        self._gateway = None
        self._address = None
        self._netmask = None
        self._enabled = None
        self._entity_scope = None
        self._external_id = None
        
        self.expose_attribute(local_name="dns_address", remote_name="DNSAddress", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="last_updated_by", remote_name="lastUpdatedBy", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="gateway", remote_name="gateway", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="address", remote_name="address", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="netmask", remote_name="netmask", attribute_type=str, is_required=False, is_unique=False)
        self.expose_attribute(local_name="enabled", remote_name="enabled", attribute_type=bool, is_required=False, is_unique=False)
        self.expose_attribute(local_name="entity_scope", remote_name="entityScope", attribute_type=str, is_required=False, is_unique=False, choices=[u'ENTERPRISE', u'GLOBAL'])
        self.expose_attribute(local_name="external_id", remote_name="externalID", attribute_type=str, is_required=False, is_unique=True)
        

        # Fetchers
        
        
        self.metadatas = NUMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        
        
        self.global_metadatas = NUGlobalMetadatasFetcher.fetcher_with_object(parent_object=self, relationship="child")
        

        self._compute_args(**kwargs)

    # Properties
    
    @property
    def dns_address(self):
        """ Get dns_address value.

            Notes:
                DNS Address for Network NSPort.

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        return self._dns_address

    @dns_address.setter
    def dns_address(self, value):
        """ Set dns_address value.

            Notes:
                DNS Address for Network NSPort.

                
                This attribute is named `DNSAddress` in VSD API.
                
        """
        self._dns_address = value

    
    @property
    def last_updated_by(self):
        """ Get last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        return self._last_updated_by

    @last_updated_by.setter
    def last_updated_by(self, value):
        """ Set last_updated_by value.

            Notes:
                ID of the user who last updated the object.

                
                This attribute is named `lastUpdatedBy` in VSD API.
                
        """
        self._last_updated_by = value

    
    @property
    def gateway(self):
        """ Get gateway value.

            Notes:
                IP address of the gateway bound to the Network NSPort.

                
        """
        return self._gateway

    @gateway.setter
    def gateway(self, value):
        """ Set gateway value.

            Notes:
                IP address of the gateway bound to the Network NSPort.

                
        """
        self._gateway = value

    
    @property
    def address(self):
        """ Get address value.

            Notes:
                IP address of the Network NSPort.

                
        """
        return self._address

    @address.setter
    def address(self, value):
        """ Set address value.

            Notes:
                IP address of the Network NSPort.

                
        """
        self._address = value

    
    @property
    def netmask(self):
        """ Get netmask value.

            Notes:
                IP address netmask of the Network NSPort.

                
        """
        return self._netmask

    @netmask.setter
    def netmask(self, value):
        """ Set netmask value.

            Notes:
                IP address netmask of the Network NSPort.

                
        """
        self._netmask = value

    
    @property
    def enabled(self):
        """ Get enabled value.

            Notes:
                Boolean value that states if the NSG Port static configuration needs to be applied.

                
        """
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """ Set enabled value.

            Notes:
                Boolean value that states if the NSG Port static configuration needs to be applied.

                
        """
        self._enabled = value

    
    @property
    def entity_scope(self):
        """ Get entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        return self._entity_scope

    @entity_scope.setter
    def entity_scope(self, value):
        """ Set entity_scope value.

            Notes:
                Specify if scope of entity is Data center or Enterprise level

                
                This attribute is named `entityScope` in VSD API.
                
        """
        self._entity_scope = value

    
    @property
    def external_id(self):
        """ Get external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        return self._external_id

    @external_id.setter
    def external_id(self, value):
        """ Set external_id value.

            Notes:
                External object ID. Used for integration with third party systems

                
                This attribute is named `externalID` in VSD API.
                
        """
        self._external_id = value

    

    