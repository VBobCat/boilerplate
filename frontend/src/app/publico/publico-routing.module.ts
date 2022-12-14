import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { PublicoComponent } from './publico.component';

const routes: Routes = [{ path: '', component: PublicoComponent }];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PublicoRoutingModule { }
