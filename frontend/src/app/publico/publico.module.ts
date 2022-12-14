import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { PublicoRoutingModule } from './publico-routing.module';
import { PublicoComponent } from './publico.component';
import {WindowModule} from '../../shared/window/window.module';


@NgModule({
  declarations: [
    PublicoComponent
  ],
    imports: [
        CommonModule,
        PublicoRoutingModule,
        WindowModule,
    ],
})
export class PublicoModule { }
