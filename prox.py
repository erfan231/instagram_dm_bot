from selenium import webdriver

        # myProxy = "127.0.0.1:9150"
        myProxy = "192.168.103.1:1081"
        ip, port = myProxy.split(":")
        fp = webdriver.FirefoxProfile()
        fp.set_preference('network.proxy.type', 1)
        fp.set_preference('network.proxy.socks', ip)
        fp.set_preference('network.proxy.socks_port', int(port))
        driver = webdriver.Firefox(fp)