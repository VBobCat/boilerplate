import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { WindowComponent } from './window.component';
import { ToolbarComponent } from './toolbar/toolbar.component';
import { PanelComponent } from './panel/panel.component';
import {MatToolbarModule} from '@angular/material/toolbar';
import {MatSidenavModule} from '@angular/material/sidenav';



@NgModule({
  declarations: [
    WindowComponent,
    ToolbarComponent,
    PanelComponent,
  ],
  imports: [
    CommonModule,
    MatToolbarModule,
    MatSidenavModule,
  ],
  exports: [
    WindowComponent,
  ],
})
export class WindowModule { }
