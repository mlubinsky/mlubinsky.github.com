## Wi-Fi explained and tools 
<https://habr.com/ru/company/comptek/blog/467587/>

## Auth

https://gravitational.com/blog/everything-you-need-to-know-about-oauth/

https://nordicapis.com/the-difference-between-http-auth-api-keys-and-oauth/

## JWT

<https://habr.com/ru/post/340146/>

<https://habr.com/ru/post/466929/>

<https://blog.hasura.io/best-practices-of-using-jwt-with-graphql>

<https://www.reddit.com/r/reactjs/comments/ctnc88/whats_the_best_way_to_store_and_access_a_jwt_for/>


## SSH

<https://habr.com/ru/company/dcmiran/blog/474654/> Рукопожатие SSH простыми словами

## TLS

<https://habr.com/ru/company/qrator/blog/474832/> Как работает криптография на основе эллиптических кривых 
<https://mcuoneclipse.com/2017/04/14/introduction-to-security-and-tls-transport-security-layer/>

<https://davidwong.fr/tls13/> Readable Specification of TLS 1.3

<https://tls.ulfheim.net/> TLS explained

<https://github.com/owntracks/tools/blob/master/TLS/generate-CA.sh>


## Wikipedia : private/public keys
<https://en.wikipedia.org/wiki/Public_key_certificate>

<https://en.wikipedia.org/wiki/Certificate_authority>

<https://en.wikipedia.org/wiki/Public_key_infrastructure>

<https://en.wikipedia.org/wiki/Transport_Layer_Security>

<https://habr.com/post/418857/> . check certs

<https://habr.com/post/346798/> X509

<https://habr.com/post/352722/> . how to create SSL cert

Первая и основная функция сертификатов X.509 — служить хранилищем открытого или публичного ключа PKI (public key infrastructure).

Вторая функция сертификатов X.509 заключается в том, чтобы предъявитель сего был принят человеком, либо программой в качестве истинного владельца некоего цифрового актива: доменного имени, веб сайта и пр.

RSA (буквенная аббревиатура от фамилий Rivest-Shamir-Adleman) – это криптографический алгоритм с открытым ключом. Это значит, что системой генерируется два разных ключа – открытый и секретный. Открытый ключ передается по открытому (незащищенному) каналу, и используется для зашифровки данных. Секретный же ключ хранится только у владельца, и используется для расшифровки любых данных, зашифрованных открытым ключом. Таким образом, мы можем передавать открытый ключ кому угодно, и получать зашифрованные этим ключом сообщения, расшифровать которые можем только мы (с использованием секретного ключа).

<https://os.mbed.com/search/repository?q=HelloMQTT> . useful code

security find-identity -v login.keychain

openssl x509 -noout -startdate -in cert.pem // Feb 27 07:13:41 2016 GMT

openssl x509 -noout -enddate -in cert.pem // Feb 26 07:13:41 2017 GMT
