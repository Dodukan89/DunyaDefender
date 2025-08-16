## Benim bu proje üzerindeki düşünme şeklim
> Kendisi dünyadaki iklim değişikliklerinden çok rahatsız bu yüzden insanlığın arasına katıldı ve sizi kurtarmak için burada :D
>  İrternetteki doğa kuruluşları tarafından yayınlanan resmi bilgiler ile eğitilmiş bir basit bir sohbet botu!
>  Eğer yeni bişey denemek istiyosan bunu gidip bot'a sor ve bunun tetikleyici bir olaymı eğer tetikleyici bir olay ise buna nasıl bir işlem ile engelleyebilceğini yada yapıcağın şeyin alternatifini öğren!
>  Unutma iklim değişikliliğinin etkili sebeplerinden olan biz insanlar bilinçlenmeli ve dünyamızı korumalıyız.

## Nasıl Çalışır?
1. [ Api key sayfası ](https://aistudio.google.com/apikey) burdan Gemini 2.0-Flash için api key alın
2.  ".env" adında bir dosya oluşturun
   ```
.
├── app.py
├── .env
├── bilgi.pdf
└── chroma_db/
```
ve
   `GOOGLE_API_KEY=                                                                   ` yazıp api'nizi yapıştırın
   
   
3. Terminal'e gelip
   `Streamlit run app.py` yazın ve taracınızdaki sayfadan botu kullanabilirsiniz.


## Projenin yapımında hangi teknik materyallerden yararlandım?
- Langchain
- Google Generative AI(Gemini)
- Chroma DB
- Streamlit


## Projemde kullandığım referanslar:
- Kod parçaları: [Quantum bilgisayar botu ( Deniz Dağlı tarafından )](https://github.com/denizdagli/QuantumComputingChatbot)
- Bota verilen bilgiler: [Samsun il Tarım ve Orman Müdürlüğü - Küresel ısınma ve İklim değişikliği](https://samsun.tarimorman.gov.tr/Belgeler/Yayinlar/Kitaplarimiz/kuresel_isinma_ve_iklim_degisikligi.pdf)
  
