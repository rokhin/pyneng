# -*- coding: utf-8 -*-
"""
Created on Sat Oct 28 22:06:19 2017

@author: 1
"""
print('Input interface')
interface_id = input()
print('Input Vlan')
vlan_id = int(input())
interface = """
interface FastEthernet0/{}
 switchport access vlan {}
 switchport portsecurity 
 spanningtree poertfast
 duplex full
"""

print(interface.format(interface_id,vlan_id))