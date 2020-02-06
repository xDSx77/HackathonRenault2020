import { Component, OnInit, Input } from '@angular/core';
import { Way } from '../wayModel';


@Component({
  selector: 'app-way',
  templateUrl: './way.component.html',
  styleUrls: ['./way.component.scss']
})
export class WayComponent implements OnInit {

  @Input() currentWay: Way;

  constructor() {
    console.log(this.currentWay);
  }


  ngOnInit() {
  }

}
