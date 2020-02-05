import { Component, OnInit } from '@angular/core';
import { ContextService } from '../context.service';
import { Observable } from 'rxjs';
import { Air } from '../air.enum';

@Component({
  selector: 'app-current-air',
  templateUrl: './current-air.component.html',
  styleUrls: ['./current-air.component.scss']
})
export class CurrentAirComponent implements OnInit {
  currentAir$: Observable<Air>;

  constructor(private contextService: ContextService) { }

  ngOnInit() {
    this.currentAir$ = this.contextService.getCurrentAir$();
  }
}
