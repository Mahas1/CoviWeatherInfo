from speedtest import Speedtest

speedtest = Speedtest()


def test_speed():
    print("Testing Download...")
    speedtest.download()
    print("Testing Upload")
    speedtest.upload()
    result_dict = speedtest.results.dict()
    download = round((result_dict.get("download") / 1000000), 2)
    upload = round((result_dict.get("upload") / 1000000), 2)
    ping = round(result_dict.get("ping"), 2)
    server_region, server_name = result_dict.get("server").get("name"), result_dict.get("server").get("sponsor")
    sent, recieved = int(result_dict.get("bytes_sent")) / 1000000, int(result_dict.get("bytes_received")) / 1000000
    return ping, upload, download, server_name, server_region, sent, recieved
