import { Component } from '@angular/core';
import { NavController } from 'ionic-angular';
import { WaterLevelPage } from '../water-level/water-level';
import { RainfallLevelPage } from '../rainfall-level/rainfall-level';
import { DataAnalysisPage } from '../data-analysis/data-analysis';


@Component({
  selector: 'page-data-display',
  templateUrl: 'data-display.html'
})
export class DataDisplayPage {

  constructor(public navCtrl: NavController) {
  }

  goToWaterLevel(params){
    if (!params) params = {};
    this.navCtrl.push(WaterLevelPage);
  }goToRainFallLevel(params){
    if (!params) params = {};
    this.navCtrl.push(RainfallLevelPage);
  }goToDataAnalysis(params){
    if (!params) params = {};
    this.navCtrl.push(DataAnalysisPage);
  }
}
