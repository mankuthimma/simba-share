from django.shortcuts import render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
import Pyro.util
import Pyro.core
import ldap

Pyro.core.initClient()

def index(request):

    # Shares
    sc = Pyro.core.getProxyForURI("PYRONAME://:smbshare.op")
    shares = sc.listshares()

    # Groups
    l = ldap.initialize("ldap://192.168.1.5")
    l.simple_bind_s("","")
    g = l.search_s("dc=intra,dc=informedia,dc=in", ldap.SCOPE_SUBTREE, "objectClass=posixGroup", ['displayName','memberUid'])

    groups = []
    for ele in g:
        tp = {}
        if (ele[1].has_key('displayName') and ele[1]['displayName'][0] == ""):
            continue
        if (ele[1].has_key('displayName')):
            tp['name'] = ele[1]['displayName'][0]
        if (ele[1].has_key('memberUid')):
            tp['members'] = ele[1]['memberUid']
        groups.append(tp)

    return render_to_response('manager/index.html', {'shares': shares,'groups': groups})


def remove(request, sharename=None):
    
    # Shares
    sc = Pyro.core.getProxyForURI("PYRONAME://:smbshare.op")
    if ( sharename is not None ):
        sc.remshare(sharename)
    shares = sc.listshares()

    # Groups
    l = ldap.initialize("ldap://192.168.1.5")
    l.simple_bind_s("","")
    g = l.search_s("dc=intra,dc=informedia,dc=in", ldap.SCOPE_SUBTREE, "objectClass=posixGroup", ['displayName','memberUid'])
    
    groups = []
    for ele in g:
        tp = {}
        if (ele[1].has_key('displayName') and ele[1]['displayName'][0] == ""):
            continue
        if (ele[1].has_key('displayName')):
            tp['name'] = ele[1]['displayName'][0]
        if (ele[1].has_key('memberUid')):
            tp['members'] = ele[1]['memberUid']
        groups.append(tp)

    return render_to_response('manager/index.html', {'shares': shares,'groups': groups})

def edit(request, sharename=None):

    # Shares
    sc = Pyro.core.getProxyForURI("PYRONAME://:smbshare.op")
    if ( sharename is not None ):
        sc.getshare(sharename)
    share = sc.getshare(sharename)

    # Groups
    l = ldap.initialize("ldap://192.168.1.5")
    l.simple_bind_s("","")
    g = l.search_s("dc=intra,dc=informedia,dc=in", ldap.SCOPE_SUBTREE, "objectClass=posixGroup", ['displayName','memberUid'])

    groups = []
    for ele in g:
        tp = {}
        if (ele[1].has_key('displayName') and ele[1]['displayName'][0] == ""):
            continue
        if (ele[1].has_key('displayName')):
            tp['name'] = ele[1]['displayName'][0]
        if (ele[1].has_key('memberUid')):
            tp['members'] = ele[1]['memberUid']
        groups.append(tp)
    
    return render_to_response('manager/edit.html', {'share': share,'groups': groups})

def modify(request):
    
    # Shares
    sc = Pyro.core.getProxyForURI("PYRONAME://:smbshare.op")

    try:
        name = request.POST['name']
        path = request.POST['path']
        comment = request.POST['comment']
        group = request.POST['group']
        sc.modshare(name, comment, path, group)
    except (KeyError, Manager.DoesNotExist):
        return render_to_response('manager/edit.html', {
            'error_message': "Form Incomplete"
        })
    else:
        return HttpResponseRedirect('index')


    # Groups
    l = ldap.initialize("ldap://192.168.1.5")
    l.simple_bind_s("","")
    g = l.search_s("dc=intra,dc=informedia,dc=in", ldap.SCOPE_SUBTREE, "objectClass=posixGroup", ['displayName','memberUid'])


    groups = []
    for ele in g:
        tp = {}
        if (ele[1].has_key('displayName') and ele[1]['displayName'][0] == ""):
            continue
        if (ele[1].has_key('displayName')):
            tp['name'] = ele[1]['displayName'][0]
        if (ele[1].has_key('memberUid')):
            tp['members'] = ele[1]['memberUid']
        groups.append(tp)
    
    return render_to_response('manager/edit.html', {'share': share,'groups': groups})


def form(request):

    sc = Pyro.core.getProxyForURI("PYRONAME://:smbshare.op")
    # Groups
    l = ldap.initialize("ldap://192.168.1.5")
    l.simple_bind_s("","")
    g = l.search_s("dc=intra,dc=informedia,dc=in", ldap.SCOPE_SUBTREE, "objectClass=posixGroup", ['displayName','memberUid'])

    groups = []
    for ele in g:
        tp = {}
        if (ele[1].has_key('displayName') and ele[1]['displayName'][0] == ""):
            continue
        if (ele[1].has_key('displayName')):
            tp['name'] = ele[1]['displayName'][0]
        if (ele[1].has_key('memberUid')):
            tp['members'] = ele[1]['memberUid']
        groups.append(tp)
    return render_to_response('manager/form.html', {'groups': groups})

def add(request):
    
    # Shares
    sc = Pyro.core.getProxyForURI("PYRONAME://:smbshare.op")

    try:
        name = request.POST['name']
        path = request.POST['path']
        comment = request.POST['comment']
        group = request.POST['group']
        sc.addshare(name, comment, path, group)
    except (KeyError, Manager.DoesNotExist):
        return render_to_response('manager/form.html', {
            'error_message': "Form Incomplete"
        })
    else:
        return HttpResponseRedirect('index')
