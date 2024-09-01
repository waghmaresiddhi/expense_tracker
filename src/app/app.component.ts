import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  // State to determine which component to display
  showLogin = true;
  showRegister = false;
  showDashboard = false;

  // Methods to switch between components
  displayLogin() {
    this.showLogin = true;
    this.showRegister = false;
    this.showDashboard = false;
  }

  displayRegister() {
    this.showLogin = false;
    this.showRegister = true;
    this.showDashboard = false;
  }

  displayDashboard() {
    this.showLogin = false;
    this.showRegister = false;
    this.showDashboard = true;
  }
}
