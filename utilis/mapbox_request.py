import shlex
import subprocess


def mapbox_request(bbox, width, height,uploaded=True):
    access_token = "access_token=pk.eyJ1Ijoib21hcnNheWVkNyIsImEiOiJja3llaXM3ZmkxOWJvMnZwYmxpNXAwNTVtIn0.XfWr-RPNuHyMSvaJE4SixQ"
    if uploaded:
        img_path='tmp_upload.png'
        cmd = 'curl -g "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/' + "[" + str(bbox[0]) + "," + str(
            bbox[1]) + "," + str(bbox[2]) + "," + str(bbox[3]) + "]" + '/' + str(width) + 'x' + str(
            height) + '?' + access_token + '"' + ' --output utilis/tmp/' + str(img_path)
        bbox_file = open("utilis/tmp/bbox.txt", "a")
        bbox_file.write( "[" + str(bbox[0]) + "," + str(bbox[1]) + "," + str(bbox[2]) + "," + str(bbox[3]) + "]")
        bbox_file.close()

    else:
        img_path = 'tmp.png'
        cmd = 'curl -g "https://api.mapbox.com/styles/v1/mapbox/satellite-v9/static/' + str(bbox) + '/' + str(width) + 'x' + str(
            height) + '?' + access_token + '"' + ' --output utilis/tmp/' + str(img_path)
        bbox_file = open("utilis/tmp/bbox.txt", "a")
        bbox_file.write(str(bbox))
        bbox_file.close()

    print(bbox)


    print(cmd)
    args = shlex.split(cmd)
    process = subprocess.Popen(
         args, shell=False, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return (stderr)