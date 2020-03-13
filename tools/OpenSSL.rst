.. OpenSSL:

OpenSSL
====================

.. image:: ../_static/OpenSSL/OpenSSL_logo.png
   :target: https://www.openssl.org/

|

OpenSSL 是一个功能极其强大的命令行工具，可以用来完成公钥体系 (Public Key Infrastructure) 
及 HTTPS 相关的很多任务。

生成证书签名请求 
------------------

如果你要从证书颁发机构(CA)获取一个SSL证书，那首先需要先生成一个证书签名请求(CSR)。
证书签名请求的主要内容是“密钥对”中的公钥，以及一些额外的信息 —— 这些内容都将在签名时插入到证书里。

当使用 OpenSSL 生成证书签名请求时，需要输入证书的唯一标识信息(Distinguished Name)，
其中重要的一项是常见名(Common Name)，它应当是你要部署证书的主机的域名全称(FQDN)。
标识信息中的其他条目用来提供关于你的机构的额外信息。
如果你从证书颁发机构购买 SSL 证书，那么通常也需要这些额外的字段，
例如组织机构(Organization)，以便能够真实地展示你的机构详情。

下面是 ``CSR`` 的模样::

   Country Name (2 letter code) [AU]:US
   State or Province Name (full name) [Some-State]:New York
   Locality Name (eg, city) []:Brooklyn
   Organization Name (eg, company) [Internet Widgits Pty Ltd]:Example Brooklyn Company
   Organizational Unit Name (eg, section) []:Technology Division
   Common Name (e.g. server FQDN or YOUR name) []:examplebrooklyn.com
   Email Address []:

也可以使用非交互方式提供生成 ``CSR`` 时要求的信息，
任何需要 CSR 信息的 OpenSSL 命令都可以添加 ``-subj`` 选项。 
例如::

   -subj "/C=US/ST=New York/L=Brooklyn/O=Example Brooklyn Company/CN=examplebrooklyn.com"

* 生成私钥和CSR

  如果你需要使用 HTTPS 来加固你的 web 服务器，那么你会向证书颁发机构申请一个证书。
  这里生成的CSR可以发送给 CA 来发行其签名的 SSL 证书。

  下面的命令创建一个2048位的私钥 (domain.key) 以及一个 CSR (domain.csr)::

     openssl req \
            -newkey rsa:2048 -nodes -keyout domain.key \
            -out domain.csr

  这里需要交互地输入 ``CSR`` 信息，以便完成整个过程。

  * ``-newkey rsa:2048``:  声明了使用 RAS 算法生成2048位的私钥
  * ``-nodes``: 表明我们不使用密码加密私钥。
  * 上面隐含了 ``-new`` 选项，表示要生成一个 CSR

* 使用已有私钥生成CSR

  如果你已经有了一个私钥，那么可以直接用它来向 CA 申请证书。

  下面的命令使用一个已有的私钥 (domain.key) 创建一个新的 CSR (domain.csr)::

     openssl req \
            -key domain.key \
            -new -out domain.csr

  * ``-key``: 用来指定已有的私钥文件
  * ``-new``: 表明我们要生成一个 CSR

* 使用已有的证书和私钥生成CSR

  如果你需要续订已有的证书，但你和CA都没有原始的 CSR，那可以再次生成 CSR。

  下面的命令使用已有的证书 (domain.crt) 和私钥 (domain.key) 创建一个新的 CSR::

     openssl x509 \
            -in domain.crt \
            -signkey domain.key \
            -x509toreq -out domain.csr

  * ``-x509toreq``: 表明我们要使用 X509 证书来制作 CSR

生成证书
------------

自签名证书
~~~~~~~~~~~

如果你只是想用 SSL 证书加固你的 web 服务器，但是并不需要 CA 签名的证书，那么一个简单的方法是自己签发证书。

一种常见的你可以签发的类型是自签名证书 —— 使用自己的私钥签发的证书。
自签名证书可以像 CA 签发的证书一样用于加密数据，但是你的用户将收到提示说明该证书不被其计算机或浏览器信息。
因此，自签名证书只能在不需要向用户证明你的身份时使用，例如非生产环境或者非公开服务。


* 生成自签名证书

  下面的命令创建一个2048位的私钥 (domain.key) 以及一个自签名证书 (domain.crt)::

     openssl req \
            -newkey rsa:2048 -nodes -keyout domain.key \
            -x509 -days 365 -out domain.crt

  * ``-x509``: 表示我们要创建自签名证书
  * ``-days 365``: 声明该证书的有效期为365天

  在上面的命令执行过程中将创建一个临时 CSR 来收集与证书相关的 CSR 信息。

* 使用已有私钥生成自签名证书
  
  下面的命令使用已有的私钥 (domain.key) 生成一个自签名证书 (domain.crt)::

     openssl req \
            -key domain.key \
            -new \
            -x509 -days 365 -out domain.crt

  * ``-new``: 用来启动CSR信息采集提示。

* 使用已有的私钥和CSR生成自签名证书

  下面的命令使用私钥 (domain.key) 和 CSR (domain.csr) 创建一个自签名证书 (domain:crt)::

     openssl x509 \
            -signkey domain.key \
            -in domain.csr \
            -req -days 365 -out domain.crt


私有CA签名证书
~~~~~~~~~~~~~~~

自签名的证书无法被吊销，CA 签名的证书可以被吊销。 能不能吊销证书的区别在于，如果你的私钥被黑客获取，
如果证书不能被吊销，则黑客可以伪装成你与用户进行通信。
 
如果你的规划需要创建多个证书，那么使用私有 CA 的方法比较合适，因为只要给所有的客户端都安装了 CA 的证书，
那么以该证书签名过的证书，客户端都是信任的，也就是安装一次就够了。

如果你直接用自签名证书，你需要给所有的客户端安装该证书才会被信任，如果你需要第二个证书，
则还的挨个给所有的客户端安装证书2才会被信任。

简单的 CA 签名可用如下方法

* 生成 CA 私钥::

     openssl genrsa -des3 -out ca.key 4096

* 生成 CA 的自签名证书::

     openssl req \
            -key ca.key \
            -new \
            -x509 -days 365 -out ca.crt
    
  其实 CA 证书就是一个自签名证书

* 生成服务端私钥::

     openssl genrsa -des3 -out server.key 2048

* 需要签名的对象（服务端）生成证书签名请求::

     openssl req \
            -key server.key \
            -new \
            -out server.csr
 
  这里注意证书签名请求当中的 ``Common Name`` 必须区别与 CA 的证书里面的 ``Common Name``。

* 用 CA 证书给生成的签名请求进行签名::

     openssl x509 \
            -CA ca.crt -CAkey ca.key \
            -req -days 365 -in server.csr -set_serial 01 -out server.crt

关于在主机上创建一个证书颁发机构的方法，请参见 `私有证书颁发机构`_ 。

查看证书
---------

证书和 CSR 文件都采用 PEM 编码格式，并不适合人类阅读。这一部分主要介绍 OpenSSL 中查看 PEM 编码文件的命令。

* 查看 CSR 文件的明文文本并进行验证::
  
     openssl req -text -noout -verify -in domain.csr

* 查看证书证书文件的明文文本::

     openssl x509 -text -noout -in domain.crt

* 验证证书 doman.crt 是否由证书颁发机构 (ca.crt) 签发::

     openssl verify -verbose -CAFile ca.crt domain.crt

私钥生成与验证
---------------

* 创建私钥

  创建一个密码保护的2048位私钥 (domain.key) ::

     openssl genrsa -des3 -out domain.key 2048

  此命令会提示输入密码。

* 验证私钥

  验证私钥 (domain.key) 是否有效::

     openssl rsa -check -in domain.key

  如果私钥是加密的，命令会提示输入密码，验证密码成功则会显示不加密的私钥。

* 验证私钥与证书和CSR匹配

  验证私钥 (domain.key) 是否与证书 (domain.crt) 以及 CSR 匹配::

     openssl rsa -noout -modulus -in domain.key | openssl md5
     openssl x509 -noout -modulus -in domain.crt | openssl md5
     openssl req -noout -modulus -in domain.csr | openssl md5

  如果上面三个命令的输出一致，那么有极高的概率可以认为私钥、证书和 CSR 是相关的。

* 加密私钥

  将未加密私钥 (unencrypted.key) 加密，输出加密后的私钥 (encrypted.key) ::

     openssl rsa -des3 \
            -in unencrypted.key \
            -out encrypted.key

  此命令执行时会提示设置密码。

* 解密私钥

  将加密私钥 (encrypted.key) 解密，并输出明文 (decrypted.key) ::

     openssl rsa \
            -in encrypted.key \
            -out decrypted.key

  此命令执行时会提示输入解密密码。

证书格式转换
--------------

我们之前接触的证书都是 ``X.509`` 格式，采用 ASCII 的 PEM 编码。
还有其他一些证书编码格式与容器类型。OpenSSL 可以用来在众多不同类型之间转换证书。

* PEM转DER

  将PEM编码的证书 (domain.crt) 转换为二进制 DER 编码的证书 (domain.der) ::

     openssl x509 \
            -in domain.crt \
            -outform der -out domain.der

  DER 格式通常用于 Java。

* DER转PEM

  将DER编码的证书 (domain.der) 转换为 PEM 编码 (domain.crt) ::

     openssl x509 \
            -inform der -in domain.der \
            -out domain.crt

* PEM转PKCS7
  
  将PEM证书 (domain.crt 和 ca-chain.crt) 添加到一个PKCS7 (domain.p7b) 文件中::

     openssl crl2pkcs7 -nocrl \
            -certfile domain.crt \
            -certfile ca-chain.crt \
            -out domain.p7b

  * ``-certfile``: 指定要添加到PKCS7中的证书

  PKCS7 文件也被称为 P7B，通常用于 Java 的 Keystore 和微软的 IIS 中保存证书的 ASCII 文件。

* PKCS7转换为PEM

  将PKCS7文件 (domain.p7b) 转换为 PEM 文件 (domain.crt) ::

     openssl pkcs7 \
            -in domain.p7b \
            -print_certs -out domain.crt

  如果 PKCS7 文件中包含多个证书，例如一个普通证书和一个中间 CA 证书，那么输出的 PEM 文件中将包含所有的证书。

* PEM转换为PKCS12
  
  将私钥文件 (domain.key) 和证书文件 (domain.crt) 组合起来生成 PKCS12 文件 (domain.pfx) ::

    openssl pkcs12 \
           -inkey domain.key \
           -in domain.crt \
           -export -out domain.pfx

  此命令将提示你输入导出密码，可以留空不填。

  PKCS12 文件也被称为 PFX 文件，通常用于导入/导出微软 IIS 中的证书链。

* PKCS12转换为PEM

  将PKCS12文件 (domain.pfx) 转换为PEM格式 (omain.combined.crt) ::

     openssl pkcs12 \
            -in domain.pfx \
            -nodes -out domain.combined.crt

  如果 PKCS12 文件中包含多个条目，例如证书及其私钥，那么生成的 PEM 文件中将包含所有条目。

私有证书颁发机构
-----------------

OpenSSL 中一些工具可用作证书颁发机构。

证书颁发机构（CA）是签署数字证书的实体。
许多网站需要让他们的客户知道连接是安全的，因此他们向国际信任的CA（例如，VeriSign，DigiCert）支付费用为其域名签署证书。

在某些情况下，与其给像 DigiCert 那样的 CA 支付费用来获得证书，不如充当您自己的 CA 可能更有意义。
常见情况包括保护内部网站，或者向客户端颁发证书以允许它们向服务器（例如，Apache，OpenVPN）进行身份验证。

.. seealso::

   `OpenSSL Certificate Authority <https://jamielinux.com/docs/openssl-certificate-authority/index.html>`_

创建根对
~~~~~~~~~

充当证书颁发机构 (CA) 意味着处理加密的私钥对和公共证书。 
我们将创建的第一个加密对是“根对”。

**“根对”由根密钥 (ca.key.pem) 和根证书(ca.cert.pem) 组成，是您的CA的身份识别。**

通常，根 CA 不直接签署服务器或客户端证书。 根 CA 仅用于创建一个或多个中间CA，中间CA由根CA信任以代表其签署证书。 
这种方式允许根密钥尽可能保持脱机，并不被使用，因为根密钥的任何损害都是灾难性的。

.. attention::

   最佳的做法是在安全环境中创建根对。 理想情况下，这应该是一个完全加密，永久隔离互联网的计算机。 
   卸下无线网卡并用胶水填充以太网端口。

#. 准备目录

   选择一个目录 (``/root/ca``) 来存储所有密钥和证书::

      mkdir /root/ca

   创建目录结构::

      cd /root/ca
      mkdir certs crl newcerts private
      chmod 700 private
      touch index.txt
      touch index.txt.attr
      echo 1000 > serial

   ``index.txt`` 和 ``serial`` 文件充当扁平数据库文件，以跟踪签名证书。

#. 准备配置文件

   您必须为 OpenSSL 创建配置文件才能使用。 
   下载 `根CA配置文件 <https://github.com/d12y12/notes/blob/master/_static/OpenSSL/root_ca.conf>`_ 并复制到 ``/root/ca/openssl.cnf``。

   下面分部分介绍一下配置文件。

   * ``[ca]`` 

      这部分是强制性的。 在这里，我们告诉OpenSSL使用 ``[CA_default]`` 部分中的选项::

         [ ca ]
         # `man ca`
         default_ca = CA_default

   * ``[CA_default]``

      这部分包含一系列默认值。 确保声明之前选择的目录 (``/root/ca``) ::

         [ CA_default ]
         # Directory and file locations.
         dir               = /root/ca
         certs             = $dir/certs
         crl_dir           = $dir/crl
         new_certs_dir     = $dir/newcerts
         database          = $dir/index.txt
         serial            = $dir/serial
         RANDFILE          = $dir/private/.rand

         # The root key and root certificate.
         private_key       = $dir/private/ca.key.pem
         certificate       = $dir/certs/ca.cert.pem

         # For certificate revocation lists.
         crlnumber         = $dir/crlnumber
         crl               = $dir/crl/ca.crl.pem
         crl_extensions    = crl_ext
         default_crl_days  = 30

         # SHA-1 is deprecated, so use SHA-2 instead.
         default_md        = sha256

         name_opt          = ca_default
         cert_opt          = ca_default
         default_days      = 375
         preserve          = no
         policy            = policy_strict

   * ``[ policy_strict ]``

      我们将对所有根CA签名应用 ``policy_strict`` ，因为根CA仅用于创建中间CA::

         [ policy_strict ]
         # The root CA should only sign intermediate certificates that match.
         # See the POLICY FORMAT section of `man ca`.
         countryName             = match
         stateOrProvinceName     = match
         organizationName        = match
         organizationalUnitName  = optional
         commonName              = supplied
         emailAddress            = optional

   * ``[ policy_loose ]``

      我们将对所有中间CA签名应用 ``policy_loose`` ，因为中间CA用于签署来自各种第三方的服务器和客户端证书::

         [ policy_loose ]
         # Allow the intermediate CA to sign a more diverse range of certificates.
         # See the POLICY FORMAT section of the `ca` man page.
         countryName             = optional
         stateOrProvinceName     = optional
         localityName            = optional
         organizationName        = optional
         organizationalUnitName  = optional
         commonName              = supplied
         emailAddress            = optional

   * ``[ req ]``

      创建证书或证书签名请求时，将应用 ``[req]`` 部分中的选项::

         [ req ]
         # Options for the `req` tool (`man req`).
         default_bits        = 2048
         distinguished_name  = req_distinguished_name
         string_mask         = utf8only

         # SHA-1 is deprecated, so use SHA-2 instead.
         default_md          = sha256

         # Extension to add when the -x509 option is used.
         x509_extensions     = v3_ca

   * ``[ req_distinguished_name ]``

      这部分声明证书签名请求中通常需要的信息。 您可以选择指定一些默认值::

         [ req_distinguished_name ]
         # See <https://en.wikipedia.org/wiki/Certificate_signing_request>.
         countryName                     = Country Name (2 letter code)
         stateOrProvinceName             = State or Province Name
         localityName                    = Locality Name
         0.organizationName              = Organization Name
         organizationalUnitName          = Organizational Unit Name
         commonName                      = Common Name
         emailAddress                    = Email Address

         # Optionally, specify some defaults.
         countryName_default             = GN
         stateOrProvinceName_default     = Guangdong
         localityName_default            = Shenzhen
         0.organizationName_default      = Yang Ltd
         #organizationalUnitName_default =
         #emailAddress_default           =

      接下来的几部分是签名证书时可以应用的扩展。 
      例如，传递 ``-extensions v3_ca`` 命令行参数将应用 ``[v3_ca]`` 中设置的选项。

   * ``[ v3_ca ]``

      在创建根证书时应用 ``v3_ca`` 扩展::

         [ v3_ca ]
         # Extensions for a typical CA (`man x509v3_config`).
         subjectKeyIdentifier = hash
         authorityKeyIdentifier = keyid:always,issuer
         basicConstraints = critical, CA:true
         keyUsage = critical, digitalSignature, cRLSign, keyCertSign

   * ``[ v3_intermediate_ca ]``

      在创建中间证书时应用 ``v3_ca_intermediate`` 扩展::

         [ v3_intermediate_ca ]
         # Extensions for a typical intermediate CA (`man x509v3_config`).
         subjectKeyIdentifier = hash
         authorityKeyIdentifier = keyid:always,issuer
         basicConstraints = critical, CA:true, pathlen:0
         keyUsage = critical, digitalSignature, cRLSign, keyCertSign

      * ``pathlen：0``: 确保中间CA下方不再有其他证书颁发机构

   * ``[ usr_cert ]``

      在签署客户端证书(例如用于远程用户身份验证的证书)时应用 ``usr_cert`` 扩展::

         [ usr_cert ]
         # Extensions for client certificates (`man x509v3_config`).
         basicConstraints = CA:FALSE
         nsCertType = client, email
         nsComment = "OpenSSL Generated Client Certificate"
         subjectKeyIdentifier = hash
         authorityKeyIdentifier = keyid,issuer
         keyUsage = critical, nonRepudiation, digitalSignature, keyEncipherment
         extendedKeyUsage = clientAuth, emailProtection

   * ``[ server_cert ]``

      在签署服务器证书(例如用于Web服务器的证书)时应用 ``server_cert`` 扩展::

         [ server_cert ]
         # Extensions for server certificates (`man x509v3_config`).
         basicConstraints = CA:FALSE
         nsCertType = server
         nsComment = "OpenSSL Generated Server Certificate"
         subjectKeyIdentifier = hash
         authorityKeyIdentifier = keyid,issuer:always
         keyUsage = critical, digitalSignature, keyEncipherment
         extendedKeyUsage = serverAuth

   * ``[ crl_ext ]``

      在创建证书吊销列表时会自动应用 ``crl_ext`` 扩展::

         [ crl_ext ]
         # Extension for CRLs (`man x509v3_config`).
         authorityKeyIdentifier=keyid:always

   * ``[ ocsp ]``

      在签署在线证书状态协议 (OCSP) 证书时应用 ``ocsp`` 扩展::

         [ ocsp ]
         # Extension for OCSP signing certificates (`man ocsp`).
         basicConstraints = CA:FALSE
         subjectKeyIdentifier = hash
         authorityKeyIdentifier = keyid,issuer
         keyUsage = critical, digitalSignature
         extendedKeyUsage = critical, OCSPSigning

#. 创建根密钥

   创建根密钥 (ca.key.pem) 并保证绝对安全, 因为拥有根密钥的任何人都可以颁发受信任的证书。 
   使用 ``AES 256`` 加密和强密码加密根密钥::

      cd /root/ca
      openssl genrsa -aes256 -out private/ca.key.pem 4096

      Enter pass phrase for ca.key.pem: secretpassword
      Verifying - Enter pass phrase for ca.key.pem: secretpassword

      chmod 400 private/ca.key.pem

   .. attention::

      对所有根证书和中间证书颁发机构密钥使用4096位。 您仍然可以签署更短的服务器和客户端证书。

#. 创建根证书

   使用根密钥 (ca.key.pem) 创建根证书 (ca.cert.pem)::

      cd /root/ca
      openssl req -config openssl.cnf \
             -key private/ca.key.pem \
             -new -x509 -days 7300 -sha256 -extensions v3_ca \
             -out certs/ca.cert.pem

      Enter pass phrase for ca.key.pem: secretpassword
      You are about to be asked to enter information that will be incorporated
      into your certificate request.
      \-----
      Country Name (2 letter code) [CN]:CN
      State or Province Name [Guangdong]:Guangdong
      Locality Name [Shenzhen]:Shenzhen
      Organization Name [Yang Ltd]:Yang Ltd
      Organizational Unit Name []:Yang Ltd Certificate Authority
      Common Name []:Yang Ltd Root CA
      Email Address []:

      chmod 444 certs/ca.cert.pem

   给根证书一个很长的失效日期，例如二十年。 根证书过期后，CA签名的所有证书都将失效。

   .. warning::

      无论何时使用 ``req`` 工具，都必须指定要与 ``-config`` 选项一起使用的配置文件，
      否则 OpenSSL 将默认为 ``/etc/pki/tls/openssl.cnf``。

#. 验证根证书

   使用命令::

      openssl x509 -noout -text -in certs/ca.cert.pem

   输出显示:

   * 使用的签名算法
   * 证书的有效期
   * 公钥长度
   * 发行人，即签署证书的实体
   * 主题，指证书本身
   * 扩展

   颁发者和主题相同，因为证书是自签名的。 请注意，所有根证书都是自签名的::

      Signature Algorithm: sha256WithRSAEncryption
      Issuer: C = CN, ST = Guangdong, L = Shenzhen, O = Yang Ltd, OU = Yang Ltd Certificate Authority, CN = Yang Ltd Root CA
      Validity
         Not Before: Jul  4 08:44:04 2019 GMT
         Not After : Jun 29 08:44:04 2039 GMT
      Subject: C = CN, ST = Guangdong, L = Shenzhen, O = Yang Ltd, OU = Yang Ltd Certificate Authority, CN = Yang Ltd Root CA
      Subject Public Key Info:
         Public Key Algorithm: rsaEncryption
            RSA Public-Key: (4096 bit)

   输出还显示X509v3扩展。 我们应用了v3_ca扩展，因此[v3_ca]中的选项应该反映在输出中::

      X509v3 extensions:
         X509v3 Subject Key Identifier:
            6A:F6:94:92:65:96:F9:01:92:79:F7:0D:7C:A6:91:DC:EB:1B:38:37
         X509v3 Authority Key Identifier:
            keyid:6A:F6:94:92:65:96:F9:01:92:79:F7:0D:7C:A6:91:DC:EB:1B:38:37
         
         X509v3 Basic Constraints: critical
            CA:TRUE
         X509v3 Key Usage: critical
            Digital Signature, Certificate Sign, CRL Sign   

创建中间对
~~~~~~~~~~~

中间证书颁发机构 (CA) 是可以代表根CA签署证书的实体。 根CA签署中间证书，形成信任链。
使用中间 CA 的目的主要是为了安全。 根密钥可以保持脱机状态并尽可能不频繁地使用。
如果中间密钥被泄露，则根CA可以撤销中间证书并创建新的中间加密对。

#. 准备目录

   根CA文件保存在 ``/root/ca`` 中。 
   选择其他目录 (``/root/ca/intermediate``) 来存储中间CA文件::

      mkdir /root/ca/intermediate

   创建与根CA文件相同的目录结构。 创建一个 ``csr`` 目录来保存证书签名请求::

      cd /root/ca/intermediate
      mkdir certs crl csr newcerts private
      chmod 700 private
      touch index.txt
      touch index.txt.attr
      echo 1000 > serial
      echo 1000 > /root/ca/intermediate/crlnumber

   * ``crlnumber``: 用于跟踪证书吊销列表

   下载 `中间CA配置文件 <https://github.com/d12y12/notes/blob/master/_static/OpenSSL/intermediate_ca.conf>`_
   并复制到 ``/root/ca/intermediate/openssl.cnf``。

   与根CA配置文件相比，有五个选项已更改::

      [ CA_default ]
      dir             = /root/ca/intermediate
      private_key     = $dir/private/intermediate.key.pem
      certificate     = $dir/certs/intermediate.cert.pem
      crl             = $dir/crl/intermediate.crl.pem
      policy          = policy_loose

#. 创建中间密钥

   创建中间密钥 (intermediate.key.pem)。 
   使用 ``AES 256`` 加密和强密码加密中间密钥::

      cd /root/ca
      openssl genrsa -aes256 \
             -out intermediate/private/intermediate.key.pem 4096

      Enter pass phrase for intermediate.key.pem: secretpassword
      Verifying - Enter pass phrase for intermediate.key.pem: secretpassword

      chmod 400 intermediate/private/intermediate.key.pem

#. 创建中间证书

   使用中间密钥创建证书签名请求 (CSR) ::

      cd /root/ca
      openssl req -config intermediate/openssl.cnf -new -sha256 \
            -key intermediate/private/intermediate.key.pem \
            -out intermediate/csr/intermediate.csr.pem

      Enter pass phrase for intermediate.key.pem: secretpassword
      You are about to be asked to enter information that will be incorporated
      into your certificate request.
      \-----
      Country Name (2 letter code) [CN]:CN
      State or Province Name [Guangdong]:Guangdong
      Locality Name [Shenzhen]:Shenzhen
      Organization Name [Yang Ltd]:Yang Ltd
      Organizational Unit Name []:Yang Ltd Certificate Authority
      Common Name []:Yang Ltd Intermediate CA
      Email Address []:

   标识信息通常应与根CA匹配, 但是 **通用名称 (Common Name)** 必须不同。

   .. attention::

      确保指定中间CA配置文件 ``intermediate/openssl.cnf``。

   使用带有 ``v3_intermediate_ca`` 扩展名的根CA来签署中间CSR::

      cd /root/ca
      openssl ca -config openssl.cnf -extensions v3_intermediate_ca \
             -days 3650 -notext -md sha256 \
             -in intermediate/csr/intermediate.csr.pem \
             -out intermediate/certs/intermediate.cert.pem

      Enter pass phrase for ca.key.pem: secretpassword
      Sign the certificate? [y/n]: y

      chmod 444 intermediate/certs/intermediate.cert.pem

   中间证书的有效期应短于根证书, 例如十年。

   .. attention::

      确保指定根CA配置文件 ``/root/ca/openssl.cnf``。

   ``index.txt`` 文件是 OpenSSL CA 工具存储证书数据库的位置。 请勿手动删除或编辑此文件。 
   它现在应该包含一个引用中间证书的行::

      V       290701141133Z           1000    unknown /C=CN/ST=Guangdong/O=Yang Ltd/OU=Yang Ltd Certificate Authority/CN=Yang Ltd Intermediate CA

#. 验证中间证书

   和验证根证书一样，检查中间证书的详细信息是否正确::

      openssl x509 -noout -text \
             -in intermediate/certs/intermediate.cert.pem


   根据根证书验证中间证书::

      openssl verify -CAfile certs/ca.cert.pem \
              intermediate/certs/intermediate.cert.pem

   如果输出 ``OK`` 表示信任链完好无损::

      intermediate/certs/intermediate.cert.pem: OK

#. 创建证书链文件

   当应用程序(例如，Web浏览器)尝试验证由中间CA签名的证书时，它还必须根据根证书验证中间证书。 

   要完成信任链，需要创建CA证书链以呈现给应用程序::

      cat intermediate/certs/intermediate.cert.pem \
          certs/ca.cert.pem > intermediate/certs/ca-chain.cert.pem
      chmod 444 intermediate/certs/ca-chain.cert.pem

   .. attention::

      我们的证书链文件必须包含根证书，因为还没有客户端应用程序知道它。 
      更好的选择，特别是在管理内网时，是在每个需要连接的客户端上安装根证书, 在这种情况下，链文件只需要包含您的中间证书。

签署服务器和客户端证书
~~~~~~~~~~~~~~~~~~~~~~~~

我们将使用我们的中间CA签署证书。
可以在各种情况下使用这些签名证书，例如保护与Web服务器的连接或验证连接到服务的客户端。

.. hint::

   以下步骤是从证书颁发机构的角度出发的。 但是，第三方可以创建自己的私钥和证书签名请求（CSR），而无需向您透露其私钥。 
   他们为您提供CSR，而您将为他们提供已签署的证书，在这情况下，跳过创建密钥和证书的过程。

#. 创建密钥

   我们的根和中间对是4096位。服务器和客户端证书通常在一年后到期，因此我们可以安全地使用2048位。

   .. hint::

      尽管4096位比2048位稍微安全一些，但它会降低TLS握手速度并显着增加握手期间的处理器负载。因此，大多数网站使用2048位对。

   如果要创建用于Web服务器（例如，Apache）的加密对，则每次重新启动Web服务器时都需要输入此密码。 
   您可能希望省略``-aes256``选项以创建没有密码的密钥::

      cd /root/ca
      openssl genrsa -aes256 \
             -out intermediate/private/www.example.com.key.pem 2048
      chmod 400 intermediate/private/www.example.com.key.pem

#. 创建证书

   使用私钥创建证书签名请求 (CSR)。 CSR详细信息不需要与中间CA匹配。 

   * 对于服务器证书，公共名称必须是完全限定的域名(例如，www.example.com)。
   * 对于客户端证书，它可以是任何唯一标识符（例如，电子邮件地址）。 

   请注意，通用名称不能与根证书或中间证书相同。

   ::

      cd /root/ca
      openssl req -config intermediate/openssl.cnf \
             -key intermediate/private/www.example.com.key.pem \
             -new -sha256 -out intermediate/csr/www.example.com.csr.pem

      Enter pass phrase for www.example.com.key.pem: secretpassword
      You are about to be asked to enter information that will be incorporated
      into your certificate request.
      \-----
      Country Name (2 letter code) [CN]:CN
      State or Province Name [Guangdong]:Beijing
      Locality Name [Shenzhen]:Beijing
      Organization Name [Yang Ltd]:Yang Ltd
      Organizational Unit Name []:Yang Ltd Web Services
      Common Name []:www.example.com
      Email Address []:

   要创建证书，请使用中间CA对CSR进行签名。 

   * 如果要在服务器上使用证书，请使用 server_cert 扩展名。 
   * 如果证书将用于用户身份验证，请使用usr_cert扩展名。 

   证书通常有效期为一年，但CA通常会为方便起见提供额外的几天。

   ``intermediate/index.txt`` 应包含引用此新证书的行::

      V       200713143355Z           1000    unknown /C=CN/ST=Beijing/L=Beijing/O=Yang Ltd/OU=Yang Ltd Web Services/CN=www.example.com

#. 验证证书

   ::

      openssl x509 -noout -text \
             -in intermediate/certs/www.example.com.cert.pem

   发行人是中间CA. 主题是指证书本身::

      Signature Algorithm: sha256WithRSAEncryption
      Issuer: C = CN, ST = Guangdong, O = Yang Ltd, OU = Yang Ltd Certificate Authority, CN = Yang Ltd Intermediate CA
      Validity
         Not Before: Jul  4 14:33:55 2019 GMT
         Not After : Jul 13 14:33:55 2020 GMT
      Subject: C = CN, ST = Beijing, L = Beijing, O = Yang Ltd, OU = Yang Ltd Web Services, CN = www.example.com
      Subject Public Key Info:
         Public Key Algorithm: rsaEncryption
            RSA Public-Key: (2048 bit)

   输出还将显示X509v3扩展。 创建证书时，您使用了 ``server_cert`` 或 ``usr_cert`` 扩展。 
   相应配置部分中的选项将反映在输出中::

      X509v3 extensions:
         X509v3 Basic Constraints:
            CA:FALSE
         Netscape Cert Type:
            SSL Server
         Netscape Comment:
            OpenSSL Generated Server Certificate
         X509v3 Subject Key Identifier:
            1C:65:5D:28:DF:FE:40:36:C1:1A:B4:02:FD:CD:AE:B5:B5:72:BE:F3
         X509v3 Authority Key Identifier:
            keyid:A8:10:FC:02:D7:41:51:F7:56:E0:35:94:8B:8F:7D:EB:81:1C:5D:89
            DirName:/C=CN/ST=Guangdong/L=Shenzhen/O=Yang Ltd/OU=Yang Ltd Certificate Authority/CN=Yang Ltd Root CA
            serial:10:00

         X509v3 Key Usage: critical
            Digital Signature, Key Encipherment
         X509v3 Extended Key Usage:
            TLS Web Server Authentication

   使用我们之前创建的CA证书链文件 (ca-chain.cert.pem) 来验证新证书是否具有有效的信任链::

      openssl verify -CAfile intermediate/certs/ca-chain.cert.pem \
              intermediate/certs/www.example.com.cert.pem

   输出::

      intermediate/certs/www.example.com.cert.pem: OK

#. 部署证书

   现在可以将新证书部署到服务器，也可以将证书分发给客户端。 

   部署到服务器应用程序(例如，Apache)时，需要提供以下文件:

   * 链文件 (``ca-chain.cert.pem``)
   * 密钥 (``www.example.com.key.pem``)
   * 证书 (``www.example.com.cert.pem``)

   如果您从第三方签署CSR，则无法访问其私钥，因此您只需要给他们提供以下文件:

   * 链文件 (``ca-chain.cert.pem``)
   * 证书 (``www.example.com.cert.pem``)

证书撤销列表
~~~~~~~~~~~~~

证书吊销列表(CRL)提供已吊销的证书列表。 

* 客户端应用程序(如Web浏览器)可以使用 ``CRL`` 检查服务器的真实性。 
* 服务器应用程序(如Apache或OpenVPN), 可以使用 ``CRL`` 拒绝访问不再受信任的客户端。

在可公共访问的位置发布CRL(例如，``http：//example.com/intermediate.crl.pem``)。 
第三方可以从此位置获取CRL，以检查它们所依赖的任何证书是否已被撤销。

.. attention::

   一些应用程序供应商已弃用证书吊销列表(CRL)，而是使用在线证书状态协议(OCSP)。

#. 准备配置文件

   当证书颁发机构签署证书时，它通常会将CRL位置编码到证书中。 
   将 ``crlDistributionPoints`` 添加到适当的部分。 
   在我们的示例中，将其添加到 ``[server_cert]`` 部分::

      [ server_cert ]
      # ... snipped ...
      crlDistributionPoints = URI:http://example.com/intermediate.crl.pem

#. 创建CRL

   ::

      cd /root/ca
      openssl ca -config intermediate/openssl.cnf \
             -gencrl -out intermediate/crl/intermediate.crl.pem

   .. seealso::

      ca手册页的 ``CRL OPTIONS`` 部分包含有关如何创建CRL的更多信息。

   您可以使用 ``crl`` 工具检查CRL的内容::

      openssl crl -in intermediate/crl/intermediate.crl.pem -noout -text

   尚未撤销任何证书，因此输出将声明 ``No Revoked Certificates``。

   您应该定期重新创建CRL。默认情况下，CRL在30天后到期, 由 ``[CA_default]`` 部分中的 ``default_crl_days`` 控制。

#. 撤销证书

   让我们来看一个完整的例子。 

   阳正在运行Apache Web服务器，并拥有一个私有文件夹。 阳想要授权他的朋友川访问此系列。

   川创建私钥和证书签名请求(CSR)::

      cd /home/chuan
      openssl genrsa -out chuan@example.com.key.pem 2048
      openssl req -new -key chuan@example.com.key.pem \
             -out chuan@example.com.csr.pem

      You are about to be asked to enter information that will be incorporated
      into your certificate request.
      \-----
      Country Name (2 letter code) [AU]:CN
      State or Province Name (full name) [Some-State]:Guangxi
      Locality Name (eg, city) []:
      Organization Name (eg, company) [Internet Widgits Pty Ltd]:Chuan Ltd
      Organizational Unit Name (eg, section) []:
      Common Name (e.g. server FQDN or YOUR name) []:chuan@example.com
      Email Address []:

   川将她的CSR发送给阳，阳随后签名并验证证书是否有效::

      cd /root/ca
      openssl ca -config intermediate/openssl.cnf \
             -extensions usr_cert -notext -md sha256 \
             -in intermediate/csr/chuan@example.com.csr.pem \
             -out intermediate/certs/chuan@example.com.cert.pem

      Sign the certificate? [y/n]: y
      1 out of 1 certificate requests certified, commit? [y/n]: y


      openssl verify -CAfile intermediate/certs/ca-chain.cert.pem \
              intermediate/certs/chuan@example.com.cert.pem

      intermediate/certs/chuan@example.com.cert.pem: OK

   此时，``index.txt`` 文件应包含一个新条目::

      V       200713143355Z           1000    unknown /C=CN/ST=Beijing/L=Beijing/O=Yang Ltd/OU=Yang Ltd Web Services/CN=www.example.com
      V       200713151536Z           1001    unknown /C=CN/ST=Guangxi/O=Chuan Ltd/CN=chuan@example.com

   阳向川发送签名证书。 

   川在她的网络浏览器中安装证书，现在可以访问阳的私人文件夹了，手动滑稽！

   倒霉的是川被黑了，阳发现并需要立即撤销她的访问权限::

      cd /root/ca
      openssl ca -config intermediate/openssl.cnf \
             -revoke intermediate/certs/chuan@example.com.cert.pem

      Enter pass phrase for intermediate.key.pem: secretpassword
      Revoking Certificate 1001.
      Data Base Updated

   此时， ``index.txt`` 中与川的证书对应的行现在以字符R开头。 这意味着证书已被撤销::

      V       200713143355Z           1000    unknown /C=CN/ST=Beijing/L=Beijing/O=Yang Ltd/OU=Yang Ltd Web Services/CN=www.example.com
      R       200713151536Z   190704152120Z   1001    unknown /C=CN/ST=Guangxi/O=Chuan Ltd/CN=chuan@example.com

   在撤销川的证书后，阳必须重新创建CRL。

#. 服务器端使用CRL

   对于客户端证书，它通常是正在进行验证的服务器端应用程序(例如，Apache)。 此应用程序需要具有对CRL的本地访问权限。

   在刚刚的例子中，阳可以将 ``SSLCARevocationPath`` 指令添加到他的Apache配置中，并将CRL复制到他的Web服务器。
   下次川连接到Web服务器时，Apache将根据CRL检查其客户端证书并拒绝访问。

   类似地，OpenVPN 有一个 ``crl-verify`` 指令，因此它可以阻止已撤销证书的客户端。

#. 客户端使用CRL

   对于服务器证书，它通常是执行验证的客户端应用程序(例如，Web浏览器)。 此应用程序必须具有对CRL的远程访问权限。

   如果证书是使用包含 ``crlDistributionPoints`` 的扩展来签名的，则客户端应用程序可以读取此信息并从指定位置获取CRL。

   CRL分发点在证书X509v3详细信息中可见::

      X509v3 CRL Distribution Points:

            Full Name:
               URI:http://example.com/intermediate.crl.pem

在线证书状态协议
~~~~~~~~~~~~~~~~~

创建在线证书状态协议(OCSP)作为证书撤销列表(CRL)的替代方案。 与CRL类似，OCSP使请求方(例如，web浏览器)能够确定证书的撤销状态。

当CA签署证书时，它们通常会在证书中包含OCSP服务器地址(例如，http：//ocsp.example.com)。 
这与用于CRL的 ``crlDistributionPoints`` 的功能类似。

例如，当Web浏览器显示服务器证书时，它将向证书中指定的OCSP服务器地址发送查询。 
在此地址，OCSP响应程序侦听查询并以证书的撤销状态作出响应。

.. hint::

   建议尽可能使用OCSP，实际上，您只需要OCSP来获取网站证书。 某些Web浏览器已弃用或删除了对CRL的支持。

#. 准备配置文件

   要使用OCSP，CA必须将OCSP服务器位置编码到为其签名的证书中。 
   在我们的示例中，使用 ``[server_cert]`` 部分的 ``authorityInfoAccess`` 选项::

      [ server_cert ]
      # ... snipped ...
      authorityInfoAccess = OCSP;URI:http://ocsp.example.com

#. 创建OCSP对

   OCSP响应者需要用OCSP加密对来签署它发送给请求方的响应。 OCSP加密对与正在检查的证书必须由同一CA签署签名。

   创建私钥并使用AES-256加密对其进行加密::

      cd /root/ca
      openssl genrsa -aes256 \
             -out intermediate/private/ocsp.example.com.key.pem 4096

   创建证书签名请求(CSR)。 细节通常应与签名CA的细节匹配。 但是，通用名(Common Name)必须是完全限定的域名::

      cd /root/ca
      openssl req -config intermediate/openssl.cnf -new -sha256 \
            -key intermediate/private/ocsp.example.com.key.pem \
            -out intermediate/csr/ocsp.example.com.csr.pem

      Enter pass phrase for intermediate.key.pem: secretpassword
      You are about to be asked to enter information that will be incorporated
      into your certificate request.
      \-----
      Country Name (2 letter code) [CN]:CN
      State or Province Name [Guangdong]:Guangdong
      Locality Name [Shenzhen]:
      Organization Name [Yang Ltd]:Yang Ltd
      Organizational Unit Name []:Yang Ltd Certificate Authority
      Common Name []:ocsp.example.com
      Email Address []:

   使用中间CA对CSR进行签名::

      openssl ca -config intermediate/openssl.cnf \
             -extensions ocsp -days 375 -notext -md sha256 \
             -in intermediate/csr/ocsp.example.com.csr.pem \
             -out intermediate/certs/ocsp.example.com.cert.pem

   验证证书是否具有正确的X509v3扩展::

      openssl x509 -noout -text \
             -in intermediate/certs/ocsp.example.com.cert.pem

      X509v3 Key Usage: critical
         Digital Signature
      X509v3 Extended Key Usage: critical
         OCSP Signing

#. 撤销证书

   OpenSSL ocsp 工具可以充当OCSP响应器，但它仅用于测试。 有可在生产中使用的OCSP响应器，但这些超出了本文的范围。

   创建要测试的服务器证书::

      cd /root/ca
      openssl genrsa -out intermediate/private/test.example.com.key.pem 2048
      openssl req -config intermediate/openssl.cnf \
             -key intermediate/private/test.example.com.key.pem \
             -new -sha256 -out intermediate/csr/test.example.com.csr.pem
      openssl ca -config intermediate/openssl.cnf \
             -extensions server_cert -days 375 -notext -md sha256 \
             -in intermediate/csr/test.example.com.csr.pem \
             -out intermediate/certs/test.example.com.cert.pem

   在 ``localhost`` 上运行OCSP响应程序。 

   OCSP响应程序不直接在单独的CRL文件中存储撤销状态，而是直接读取 ``index.txt`` 。 
   响应使用OCSP加密对进行签名(使用 ``-rkey`` 和 ``-rsigner`` 选项)::

      openssl ocsp -port 2560 \
             -index intermediate/index.txt \
             -CA intermediate/certs/ca-chain.cert.pem \
             -rkey intermediate/private/ocsp.example.com.key.pem \
             -rsigner intermediate/certs/ocsp.example.com.cert.pem \
             -nrequest 1 \
             -text 

      Enter pass phrase for ocsp.example.com.key.pem: secretpassword

   在另一个终端中，向OCSP响应者发送查询。 ``-cert`` 选项指定要查询的证书::

      openssl ocsp -CAfile intermediate/certs/ca-chain.cert.pem \
             -url http://127.0.0.1:2560 -resp_text \
             -issuer intermediate/certs/intermediate.cert.pem \
             -cert intermediate/certs/test.example.com.cert.pem

   输出::

      OCSP Response Data:
         OCSP Response Status: successful (0x0)
         Response Type: Basic OCSP Response
         Version: 1 (0x0)
         Responder Id: C = CN, ST = Guangdong, L = Shenzhen, O = Yang Ltd, OU = Yang Ltd Certificate Authority, CN = ocsp.example.com
         Produced At: Jul  4 16:10:49 2019 GMT
         Responses:
         Certificate ID:
            Hash Algorithm: sha1
            Issuer Name Hash: 3C550CCB561AC011EBD5CA8638D2983A9DEBBAEF
            Issuer Key Hash: A810FC02D74151F756E035948B8F7DEB811C5D89
            Serial Number: 1003
         Cert Status: good
         This Update: Jul  4 16:10:49 2019 GMT

   输出的开头显示：

   * 是否收到成功回复（``OCSP Response Status``）
   * 响应者的身份（``Responder Id``）
   * 证书的撤销状态（``Cert Status``）

   撤销证书::

      openssl ca -config intermediate/openssl.cnf \
             -revoke intermediate/certs/test.example.com.cert.pem

      Enter pass phrase for intermediate.key.pem: secretpassword
      Revoking Certificate 1003.
      Data Base Updated

   和刚刚一样，运行OCSP响应器并在另一个终端上发送查询。 

   这次，输出显示 ``Cert Status：revoked`` 和 ``Revocation Time``::

      OCSP Response Data:
         OCSP Response Status: successful (0x0)
         Response Type: Basic OCSP Response
         Version: 1 (0x0)
         Responder Id: C = CN, ST = Guangdong, L = Shenzhen, O = Yang Ltd, OU = Yang Ltd Certificate Authority, CN = ocsp.example.com
         Produced At: Jul  4 16:17:29 2019 GMT
         Responses:
         Certificate ID:
            Hash Algorithm: sha1
            Issuer Name Hash: 3C550CCB561AC011EBD5CA8638D2983A9DEBBAEF
            Issuer Key Hash: A810FC02D74151F756E035948B8F7DEB811C5D89
            Serial Number: 1003
         Cert Status: revoked
         Revocation Time: Jul  4 16:16:18 2019 GMT
         This Update: Jul  4 16:17:29 2019 GMT
