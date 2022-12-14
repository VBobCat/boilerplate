import {NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import {RaizComponent} from './raiz/raiz.component';

const routes: Routes = [
  {
    path: '', pathMatch: 'full', component: RaizComponent,
  },
  {
    path: 'publico', loadChildren: () => import('./publico/publico.module').then(m => m.PublicoModule),
  },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule],
})
export class AppRoutingModule {
}
