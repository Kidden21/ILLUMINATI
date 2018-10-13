import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { AngularFirestore } from 'angularfire2/firestore'


@Component({
  selector: 'page-water-level',
  templateUrl: 'water-level.html'
})
export class WaterLevelPage {

  _db:AngularFirestore;
  waterlevel: any = [];
  selectedDA: any;
  constructor(
    public navCtrl: NavController,
    public db: AngularFirestore) {
      db.collection<any>('WaterLevel')
        .valueChanges()
        .subscribe(d => {
          this.waterlevel = d;
        });
      this._db = db;
  }

  HandleSelection(data) {
    this.selectedDA = data;
  }

  public barChartOptions:any = {
  scaleShowVerticalLines: false,
  responsive: true
};
public barChartLabels:string[] = ['January', 'February', 'March', 'April', 'May', 'June', 'July'];
public barChartType:string = 'bar';
public barChartLegend:boolean = true;

public barChartData:any[] = [
  {data: [2981, 2712, 2652, 2512, 2811, 2920, 2810], label: 'Kuala Pari'},
];
public barChartData2:any[] = [
  {data: [1611, 1711, 1632, 1532, 1677, 1512, 1431], label: 'Parit'},
];

public barChartColors:Array<any> = [
  { // dark grey
    backgroundColor: 'rgba(77,83,96,0.2)',
    borderColor: 'rgba(77,83,96,1)',
    pointBackgroundColor: 'rgba(77,83,96,1)',
    pointBorderColor: '#fff',
    pointHoverBackgroundColor: '#fff',
    pointHoverBorderColor: 'rgba(77,83,96,1)'
  },
];

// events
public chartClicked(e:any):void {
  console.log(e);
}

public chartHovered(e:any):void {
  console.log(e);
}

// public randomize():void {
//   // Only Change 3 values
//   let data = [
//     Math.round(Math.random() * 100),
//     59,
//     80,
//     (Math.random() * 100),
//     56,
//     (Math.random() * 100),
//     40];
//   let clone = JSON.parse(JSON.stringify(this.barChartData));
//   clone[0].data = data;
//   this.barChartData = clone;
//   /**
//    * (My guess), for Angular to recognize the change in the dataset
//    * it has to change the dataset variable directly,
//    * so one way around it, is to clone the data, change it and then
//    * assign it;
//    */
// }
}
