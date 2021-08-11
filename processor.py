import os

f=open("login.txt","r")
lines=f.readlines()
username=lines[0]
password=lines[1]

def download_xml(self, url, product, out_path, login):
    user_name = username
    user_password = password

    command = "wget --no-verbose --no-check-certificate --output-document={out} {url}".format(out=out_path, url=url + product)
    if login:
        command = "wget --no-verbose --no-check-certificate --user={user} --password={pwd} --output-document={out}"\
                  " {url}".format(user=user_name, pwd=user_password, out=out_path, url=(url + product))

    self.info("Downloading product as " + command)
    error_code, error_msg = utilities.execute(command)
    if error_code != 0:
        raise RuntimeError("Failed to download product {}. Error code: {}, error message:\n{}"
                           .format(product, error_code, error_msg))
    if login:
        time.sleep(1.5)  # scihub does not allow too frequent queries; therefore wait a bit before a new query
