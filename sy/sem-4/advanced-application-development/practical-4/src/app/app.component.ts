import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit  {
  title = 'exception-handling';

  ngOnInit(){
    throw new Error("This error is meant to handled by the error handler service.")
  }



}
