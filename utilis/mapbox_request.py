import shlex
import subprocess


def mapbox_request(bbox, width, height):
    access_token = "access_token=pk.eyJ1Ijoib21hcnNheWVkNyIsImEiOiJja3llaXM3ZmkxOWJvMnZwYmxpNXAwNTVtIn0.XfWr-RPNuHyMSvaJE4SixQ"
    cmd = 'curl -g "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/' +"["+str(bbox[0])+","+str(bbox[1])+","+str(bbox[2])+","+str(bbox[3])+"]"+'/'+str(width)+'x'+str(height)+'?'+access_token+'"' + ' --output utilis/tmp/tmp.png'
    print(cmd)
    args = shlex.split(cmd)
    process = subprocess.Popen(
         args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return (stderr)