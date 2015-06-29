# QuickMeds
####BattleHack Chicago 2015

QuickMed brings availability of over-the-counter meds into the 21st century. Although the field of medicine has advanced tremendously over the last decade, technology has not kept pace. There is no aggregated source for medical data, and customers (especially in rural areas or developing countries) have no way to easily locate essential medications such as epipens. This would involve an arduous process of contacting multiple clinics when time may be of the essence.

##iOS App
Our mobile application takes your location and automatically aggregates the closest clinics that have your required medication. Information is accurate and up-to-date so that you can rest easy!

![iOS Search](https://raw.githubusercontent.com/MAKE-UIUC/BHChi15/master/iOS/mkt/iOS%20Search%20Page.png)
![iOS Map](https://raw.githubusercontent.com/MAKE-UIUC/BHChi15/master/iOS/mkt/iOS%20Map.png)

##SMS FrameWork
We also recognize that a majority of people in the world do not have stable internet. In order to implement our solution for those who need it most, we created a purely SMS-based system that queries your location and finds the nearest pharmacies near you who have what you need. Through Twillio and Paypal, this service will buy the medication for you.

##Web App
Another huge problem in the pharmaceutical industry is data and record keeping. Our web infrastructure allows pharmacies to easily track their stores in real time, and also receives orders for medications from our mobile apps.

##Backend / API
These tools are all built on a robust REST api framework, the documentation for which you can see here: https://github.com/MAKE-UIUC/BHChi15/blob/master/endpoints.md

This REST API lays the groundwork for a centralized pharmaceutical record-keeping system whose information can be used to prepare for disease outbreaks and predict trends in health.


##Check Us Out
You can check out our technology stack here: https://github.com/MAKE-UIUC/BHChi15/blob/master/endpoints.md

and our repo here: https://github.com/MAKE-UIUC/BHChi15

We hope our app can be applied to make your world a healthier place!
