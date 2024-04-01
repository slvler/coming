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
- [Amazon EBS](#ebs)
- [Autoscaler](#autoscaler)
- [Load Balancer](#load-balancer)
- [Lambda](#lambda)



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


<a name="ebs"></a>
## Amazon Elastic Block Store
- bu servis depolama alanı olarak özel alan belirlenmesini sağlar

<a name="autoscaler"></a>
## Autoscaler

<a name="load-balancer"></a>
## Load Balancer

<a name="lambda"></a>
## Lambda