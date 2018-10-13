import { Component } from '@angular/core';
import { HomePage } from '../home/home';
import { HotlineInfoPage } from '../hotline-info/hotline-info';
import { DataDisplayPage } from '../data-display/data-display';
import { SocialSharingPage } from '../social-sharing/social-sharing';
import { EvacuationSystemPage } from '../evacuation-system/evacuation-system';


@Component({
  selector: 'page-tabs',
  templateUrl: 'tabs.html'
})
export class TabsPage {

    //Tabs Navigation pages
    tab1Root = HomePage;
    tab2Root = EvacuationSystemPage;
    tab3Root = DataDisplayPage;
    tab4Root = SocialSharingPage;
    tab5Root = HotlineInfoPage;

}
