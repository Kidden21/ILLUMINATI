import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { MoreInfoPage } from '../more-info/more-info';
import { AngularFirestore } from 'angularfire2/firestore'

@Component({
  selector: 'page-data-analysis',
  templateUrl: 'data-analysis.html'
})
export class DataAnalysisPage {

  _db:AngularFirestore;
  datanalysis: any = [];
  selectedDA: any = {
    Date: '',
    Time: '',
    Increment: '',
    Message: '',
    Flood_Risk_Score: '',
    Population_Score: '',
    Flood_Severity: ''
  };

  constructor(
    public navCtrl: NavController,
    public db: AngularFirestore) {
      db.collection<any>('data_analysis')
        .valueChanges()
        .subscribe(d => {
          this.datanalysis = d;
        });
      this._db = db;
  }
  SwitchMoreInfo(params){
    if (!params) params = {};
    this.navCtrl.push(MoreInfoPage);
  }
  HandleSelection(data) {
    this.selectedDA = data;
  }
}
