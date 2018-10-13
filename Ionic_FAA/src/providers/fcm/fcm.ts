import { Injectable } from '@angular/core';
import { Firebase } from '@ionic-native/firebase';
import { Platform } from 'ionic-angular';
import { AngularFirestore } from 'angularfire2/firestore';
import { Geolocation } from '@ionic-native/geolocation';


@Injectable()
export class FcmProvider {
  public latitude:any;
  public longitude:any;
  constructor(
    public firebaseNative: Firebase,
    public afs: AngularFirestore,
    public geolocation: Geolocation,
    private platform: Platform
    ) {
      this.geolocation.getCurrentPosition().then((resp) => {
         this.latitude=resp.coords.latitude;
         this.longitude=resp.coords.longitude;
      }).catch((error) => {
        console.log('Error getting location'+JSON.stringify(error));
      });
    }

  async getToken() {

    let token;

    if (this.platform.is('android')) {
      token = await this.firebaseNative.getToken()
    }

    if (this.platform.is('ios')) {
      token = await this.firebaseNative.getToken();
      await this.firebaseNative.grantPermission();
    }

    return this.saveTokenToFirestore(token)
  }

  async getTokGeo(){
    let geo;
    let token;

    if (this.platform.is('android')) {
      token = await this.firebaseNative.getToken()
    }

    if (this.platform.is('ios')) {
      token = await this.firebaseNative.getToken();
      await this.firebaseNative.grantPermission();
    }

    geo = this.latitude+', '+this.longitude;
    return this.saveTokGeoToFirestore(token, geo)
  }

  private saveTokenToFirestore(token) {
    if (!token) return;

    const devicesRef = this.afs.collection('devices')

    const docData = {
      token,
      userId: 'testUser',
    }

    return devicesRef.doc(token).set(docData)
  }

  private saveTokGeoToFirestore(token, geo) {

    const devicesRef = this.afs.collection('tokenLocations')

    const docData = {
      token,
      geo,
    }

    return devicesRef.doc(token).set(docData)
  }

  listenToNotifications() {
  return this.firebaseNative.onNotificationOpen()
  }
}
