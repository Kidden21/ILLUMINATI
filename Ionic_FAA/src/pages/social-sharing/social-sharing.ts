import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { Camera, CameraOptions } from '@ionic-native/camera';
import { SocialSharing } from '@ionic-native/social-sharing';
import { Geolocation } from '@ionic-native/geolocation';


@Component({
  selector: 'page-social-sharing',
  templateUrl: 'social-sharing.html'
})
export class SocialSharingPage {

  captureDataUrl: string;
  public latitude:any;
  public longitude:any;

  constructor(public navCtrl: NavController,
              private camera: Camera,
              private sharingVar: SocialSharing,
              private geolocation: Geolocation,) {
                this.geolocation.getCurrentPosition().then((resp) => {
                   this.latitude=resp.coords.latitude;
                   this.longitude=resp.coords.longitude;
                }).catch((error) => {
                  console.log('Error getting location'+JSON.stringify(error));
                });
               }

  takePhoto() { //funtion to takephoto or upload from photo album
    const cameraOptions: CameraOptions = {
      quality: 100,
      destinationType: this.camera.DestinationType.DATA_URL,
      encodingType: this.camera.EncodingType.JPEG,
      mediaType: this.camera.MediaType.PICTURE,
    };

    this.camera.getPicture(cameraOptions).then((imageData) => {
      // imageData is either a base64 encoded string or a file URI
      // If it's base64:
      this.captureDataUrl = 'data:image/jpeg;base64,' + imageData;
    }, (err) => {
      // Handle error
    });
  }


//sharing function using ionic-social-sharing plugin
  whatsappShare(){
    this.sharingVar.shareViaWhatsApp('Flood Aid Needed at this location! '+this.latitude+', '+this.longitude /*Message*/, this.captureDataUrl /*Image*/,  null /* url */)
      .then(()=>{
      },
      ()=>{
         alert("WhatsApp Sharing failed")
      })
    }


  facebookShare(){
    this.sharingVar.shareViaFacebook('Flood Aid Needed at this location! '+this.latitude+', '+this.longitude /*Message*/, this.captureDataUrl /*Image*/,  null /* url */)
      .then(()=>{
      },
      ()=>{
         alert("Facebook Sharing failed")
      })
    }


  twitterShare(){
    this.sharingVar.shareViaTwitter('Flood Aid Needed at this location! '+this.latitude+', '+this.longitude /*Message*/, this.captureDataUrl /*Image*/,  null /* url */)
      .then(()=>{
      },
      ()=>{
         alert("Twitter Sharing failed")
      })
    }


  instagramShare(){
    this.sharingVar.shareViaInstagram('Flood Aid Needed at this location! '+this.latitude+', '+this.longitude /*Message*/, this.captureDataUrl /*Image*/)
      .then(()=>{
      },
      ()=>{
         alert("Instagram Sharing failed")
      })
    }


}
