import requests, argparse, json

def Main(algo, hashh, identifie):
    url = 'http://api.crackfoo.net'
    key = '<api key here>'

    if args.identifie:
        req = requests.post('http://id-api.crackfoo.net/', data={'hash':args.identifie})
        result = req.text
        load_json = json.loads(result)
        formated_json = json.dumps(load_json, indent=4)
        print(formated_json)
    elif args.hash or args.algo:
        req = requests.get(url + "?key=" + key + "&algo=" + args.algo + "&hash=" + args.hash)
        res = req.json()
        if res['Status'] == 'SUCCESS':
            final_res = """
Algorithum: {algo}
Hash: {hash}
Result: {return}
            """.format(**res)
            print(final_res)
        elif res['Status'] == 'NOTFOUND':
            print('Hash was not found in DB')
        elif res['Status'] == 'AuthFail':
            print('Missing or Invalid APIKEY')
        elif res['Status'] == 'MissingParams':
            print('Missing Algo or Hash')
        elif res['Status'] == 'InvalidAlgo':
            print('Algorithm is not Supported/Disabled')
        elif res['Status'] == 'InvalidChars':
            print('The Algorithm or Hash contains Invalid Characters')
        elif res['Status'] == 'BackendError':
            print('ContactAdmin/Get in touch. Something is seriously wrong')
        else:
            print('Unknown error has occurred')
    else:
        print('Get password for hash and algorithum if it is in the database, or identifie hash type\nUsage: crackfoo.py [options] -hash Hash_Here -algo Algorithum_Here -identifie hash_to_identifie')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Hash Database')
    ap = argparse.ArgumentParser(prog='crackfoo.py', usage='%(prog)s [options] -hash Hash_Here -algo Algorithum_Here -identifie hash_to_identifie', description='Get password for hash and algorithum if it is in the database')
    ap.add_argument('-hash', type=str, help='Input hash')
    ap.add_argument('-algo', type=str, help='Input algo (md5, sha1, lm, ntlm, cisco7)')
    ap.add_argument('-identifie', type=str, help='Input hash to identifie using HashID')
    args = ap.parse_args()
    algo = args.algo
    hashh = args.hash
    identifie = args.identifie
    Main(algo, hashh, identifie)
