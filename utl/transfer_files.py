import paramiko


def transfer_file(local_path, des_path):
    # 实例化一个trans对象# 实例化一个transport对象
    trans = paramiko.Transport(('58.34.161.11', 22220))
    # 建立连接
    trans.connect(username='xhy', password='123456')

    # 实例化一个 sftp对象,指定连接的通道
    sftp = paramiko.SFTPClient.from_transport(trans)
    sftp.put(localpath=local_path, remotepath=des_path)
    trans.close()

transfer_file("./output/json_dataset/10.3390_app13158876.json", "/home/xhy/json_dataset/10.3390_app13158876.json")