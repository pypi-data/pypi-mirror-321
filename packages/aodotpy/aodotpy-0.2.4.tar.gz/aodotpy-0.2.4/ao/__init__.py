import requests
import arseeding
from .signer import ARSigner

SDK = 'ao.py'
MU = 'https://mu.ao-testnet.xyz'
CU = 'https://cu.ao-testnet.xyz'
SCHEDULER = '_GQ33BkPtZrqxA84vM8Zk-N2aO0toNNu_C-l-rawrBA'

def get_tags(nv):
    tags = {}
    for t in nv:
        tags[t['name']] = t['value']
    return tags

def process_msg(msg):
    if not msg.get('Tags'):
        return msg
    tags = get_tags(msg['Tags'])
    msg['Tags'] = tags
    return msg

def process_result(res):
    if not res.get('Messages'):
        return res
    msgs = res['Messages']
    for msg in msgs:
        msg = process_msg(msg)
    res['Messages'] = msgs
    return res

def send_message(singer, pid, anchor, tags, data='', mu=MU, timeout=5):
    default_tags = {
        'Data-Protocol': 'ao',
        'Variant': 'ao.TN.1',
        'Type': 'Message',
        'SDK': SDK,
    }
    default_tags.update(tags)
    b = arseeding.BundleItem(singer, pid, anchor, default_tags, data)
    res = requests.post(mu, data=b.binary, headers={'Content-Type': 'application/octet-stream'}, timeout=timeout).json()
    res = process_result(res)
    return b.id, res


def dry_run(pid, anchor, tags, data='', cu=CU, timeout=30, owner='AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA'):
    default_tags = {
        'Data-Protocol': 'ao',
        'Variant': 'ao.TN.1',
        'Type': 'Message',
        'SDK': SDK,
    }
    default_tags.update(tags)

    tags = [{'name':k, 'value':v} for k,v in tags.items()]
    url = '%s/dry-run?process-id=%s' % (cu, pid)
    payload = {
        'Target': pid,
        'Owner': owner,
        'Anchor': anchor,
        'Data': data,
        'Tags': tags,
    }
    res = requests.post(url, json=payload, timeout=timeout).json()
    return process_result(res)
    
def spawn_process(singer, module, anchor, tags, data='', mu=MU, scheduler=SCHEDULER, timeout=5):
    default_tags = {
        'Data-Protocol': 'ao',
        'Variant': 'ao.TN.1',
        'Type': 'Process',
        'Scheduler':scheduler,
        'Module':module,
        'SDK': SDK,
    }
    default_tags.update(tags)
    b = arseeding.BundleItem(singer, '', anchor, default_tags, data)
    res = requests.post(mu, data=b.binary, headers={'Content-Type': 'application/octet-stream'}, timeout=timeout).json()
    res = process_result(res)
    return b.id, res

def get_result(pid, message_id, cu=CU, timeout=5):
    res = requests.get(f'{cu}/result/{message_id}?process-id={pid}', timeout=timeout).json()
    res = process_result(res)
    return res

def send_and_get(singer, pid, anchor, tags, data='', mu=MU, cu=CU, timeout=5):
    mid, _ = send_message(singer, pid, anchor, tags, data, mu, timeout)
    return mid, get_result(pid, mid, cu, timeout)
