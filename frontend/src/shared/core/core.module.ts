import {LOCALE_ID, ModuleWithProviders, NgModule} from '@angular/core';
import {CommonModule, registerLocaleData} from '@angular/common';
import localePT from '@angular/common/locales/pt';
import localeExtraPT from '@angular/common/locales/extra/pt';

registerLocaleData(localePT, 'pt', localeExtraPT);


@NgModule({
  declarations: [],
  imports: [
    CommonModule,
  ],
})
export class CoreModule {
  static forRoot(): ModuleWithProviders<CoreModule> {
    return {
      ngModule: CoreModule,
      providers: [
        {provide: LOCALE_ID, useValue: 'pt'},
      ],
    };
  }
}
