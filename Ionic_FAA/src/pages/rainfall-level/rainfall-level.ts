import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { AngularFirestore } from 'angularfire2/firestore'

@Component({
  selector: 'page-rainfall-level',
  templateUrl: 'rainfall-level.html'
})
export class RainfallLevelPage {

  _db:AngularFirestore;
  rainlevel: any = [];
  selectedDA: any;
  constructor(
    public navCtrl: NavController,
    public db: AngularFirestore) {
      db.collection<any>('RainLevel')
        .valueChanges()
        .subscribe(d => {
          this.rainlevel = d;
        });
      this._db = db;
  }

  HandleSelection(data) {
    this.selectedDA = data;
  }
  public lineChartData:Array<any> = [
  {data: [3381, 3431, 3123, 3300, 3512, 3133, 3266], label: 'Kuala Pari' },
  ];
  public lineChartData2:Array<any> = [
  {data: [3781, 3651, 3912, 3882, 3832, 3822, 3612], label: 'Parit' },
  ];
  public lineChartLabels:Array<any> = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
  public lineChartOptions:any = {
    responsive: true
  };
  public lineChartColors:Array<any> = [
    { // dark grey
      backgroundColor: 'rgba(77,83,96,0.2)',
      borderColor: 'rgba(77,83,96,1)',
      pointBackgroundColor: 'rgba(77,83,96,1)',
      pointBorderColor: '#fff',
      pointHoverBackgroundColor: '#fff',
      pointHoverBorderColor: 'rgba(77,83,96,1)'
    },
  ];
  public lineChartLegend:boolean = true;
  public lineChartType:string = 'line';

  // public randomize():void {
  //   let _lineChartData:Array<any> = new Array(this.lineChartData.length);
  //   for (let i = 0; i < this.lineChartData.length; i++) {
  //     _lineChartData[i] = {data: new Array(this.lineChartData[i].data.length), label: this.lineChartData[i].label};
  //     for (let j = 0; j < this.lineChartData[i].data.length; j++) {
  //       _lineChartData[i].data[j] = Math.floor((Math.random() * 100) + 1);
  //     }
  //   }
  //   this.lineChartData = _lineChartData;
  // }

  // events
  public chartClicked(e:any):void {
    console.log(e);
  }

  public chartHovered(e:any):void {
    console.log(e);
  }

}
