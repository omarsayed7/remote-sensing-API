import shlex
import subprocess
bbox = "[-122.44436073309774, 37.79756812813746, -122.44397020320322, 37.79791048668099]"
access_token = "access_token=pk.eyJ1Ijoib21hcnNheWVkNyIsImEiOiJja3llaXM3ZmkxOWJvMnZwYmxpNXAwNTVtIn0.XfWr-RPNuHyMSvaJE4SixQ"
width = 800
height = 800
cmd = 'curl -g "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/' + \
    bbox+'/'+str(width)+'x'+str(height)+'?'+access_token+'"' + \
    ' --output example-mapbox-static-bbox-1.png'

args = shlex.split(cmd)
process = subprocess.Popen(
    args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
stdout, stderr = process.communicate()
