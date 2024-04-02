# Cloud Konuları


## Açıklamalar

- Temel amaç cloud ortam ve platformlarının düzenlenmesi


# İçindekiler


### Aws

- [EC2](#ec2)
    - [İhtiyaç belirleme](#needs-assessment)
	- [Network](#network)
	- [Key pair](#key-pair)
    - [IAM role](#iam-role)
    - [SSH](#ssh)
- [Amazon Elastic Container Service](#ecs)
- [Amazon Simple Storage Service](#s3)
    - [bucket oluşturma](#bucket)
- [Amazon Elastic Block Store](#ebs)
- [Amazon Elastic File System](#efs)
- [Autoscaler](#autoscaler)
    - [Sabit ip](#elastic-ip)   
- [Load Balancer](#load-balancer)
- [Lambda](#lambda)
- [Network](#network)
    - [Amazon Virtual Private Cloud](#vpc)
    - [Amazon Route 53](#53)
    - [Amazon CloudFront](#cloud-front)

- [Network](#network)
    - [Amazon Virtual Private Cloud](#vpc)




<a name="ec2"></a>
## EC2

- işletim sistemi seçilen servistir
- Sistem Konfigürasyonu seçilir. İşletim sistemi, gpu, cpu, ram ve donanım ve imaj kısımlarının belirlendiği servistir.
- makina açılırken hangi programların yüklü geleceği belirlenir.

<a name="needs-assessment"></a>
### ihtiyaç belirleme 
- veritabanı kullanılıyorsa ram yüksek
- r4, r5 / 4. yada 5. jenerasyon olup yüksek ram kapasitesi sağlar
- x1e16, x1e32 / devasa işlemci gücü olan makinalar
- p2, p3 / yapay zeka için kullanılması uygundur
- m4, m5 / genel kullanım için eşit dağılım kullanılır.
- d2, d3 / local diski destekler ve diske yazma için avantajlıdır. 

- ilk kullanım için t2, t3 tipi makinalar iyidir.

<a name="network"></a>
### Network katmanı
- network seçimi sonucunda private veya public olması durumu belirlenir. dışarıdan ulaşım durumu
- subnet ayarlamak gereklidir.
- public ip ayarı yapılmalıdır.

<a name="key-pair"></a>
### Key pair
- pem dosyası, ssh bağlantısı yapmanı sağlayacak olan dosyadır.
- bir makinaya kimler bağlanacak ve hangi yetkiler ile bağlanacak bunun ayarlanmasını sağlayan pem dosyası oluşturulur.

<a name="iam-role"></a>
### IAM role
- mevcut imajı (makinayı) ayağa kaldıran kişinin rolü ve yetkisinin belirlendiği ayardır.

<a name="ssh"></a>
### SSH
- indirilen, oluşturulan pem dosyası ile ssh bağlantısı yapıyoruz

<a name="ecs"></a>
## Amazon Elastic Container Service

<a name="s3"></a>
## Amazon Simple Storage Service
- Depolama alanı olarak kullanılır.

<a name="ebs"></a>
## Amazon Elastic Block Store
- bu servis depolama alanı olarak özel alan belirlenmesini sağlar

<a name="autoscaler"></a>
## Autoscaler

- otomatik olarak sunucu alma, kiralama çoğalma durumudur. 
- örnek -> 2 makinanız var misal kampanya süresine girdi otomatik olarak 4 makinaya çıkıyorsun.
- sunucuları ölçekleme için kullanılan durumlardır.
- çeşitli satın alma durumları içinde kullanılır.

<a name="elastic-ip"></a>
### Elastic IP

- elastic ip / domain yönlendirmelerin kullanılan ip adresi
- makina kapatılıp açılınca değişmek - sabit ip

<a name="load-balancer"></a>
## Load Balancer

- otomatik olarak alınan sunuculara trafik yönlendirmek için otomatik yönlendiricidir.

<a name="lambda"></a>
## Lambda

- sunucu seçmeden kod çalıştırmaya yarar.
- request gelir işlem yapılır ve response verilir.
- misal telefon numarası geldi, gönderilecek mesaj hazırlandı, gelen telefon numarasına mesaj gönderildi. 


<a name="network"></a>
## Network

- Sunucular arasındaki bağlantılar, iletişim, erişim alanlarının düzenlenmesi

<a name="vpc"></a>
### Amazon Virtual Private Cloud

- aws tarafında kendi tanımlanan sanal ağda başlatılan erişim ortamıdır.
- alt ağ oluşturmak ve çok katmanlı güvenlik hizmeti sağlar

<a name="53"></a>
### Amazon Route 53

- dns servisidir.
- domain yönlendirme, rood balancer kurulumu hepsi bu servis içerisindedir.

<a name="cloud-front"></a>
### Amazon CloudFront

- cdn - ön bellek servisidir.
- Belge, dosya cache için kullanılır.