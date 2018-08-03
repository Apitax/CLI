# CLI
A CLI built for Apitax supporting Commandtax and Scriptax. It will also handle any and all authentication along the way


## Installation and Usage
* Clone this repository and run `pip install .`
    * It is recommended to use a Python virtual environment for this, but it is not mandatory
* Run apitax commands

### Commands
* `apitax --help`
    * In fact any sub command with `--help` attached will show you how to use the command
        * `apitax --help` -> `apitax script --help` -> `apitax script execute --help`

## Documentation for API Endpoints

All URIs are relative to *https://localhost/apitax/2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AdminsApi* | [**display_admin_dashboard**](docs/AdminsApi.md#display_admin_dashboard) | **GET** /dashboard/admin | Displays the developer admin page
*AdminsApi* | [**driver_status**](docs/AdminsApi.md#driver_status) | **GET** /system/driver/{name}/status | Retrieve the status of a loaded driver
*AdminsApi* | [**system_status**](docs/AdminsApi.md#system_status) | **GET** /system/status | Retrieve the system status
*AnyApi* | [**authenticate**](docs/AnyApi.md#authenticate) | **POST** /auth | Authenticate
*AnyApi* | [**display_login**](docs/AnyApi.md#display_login) | **GET** /login | Displays the login page
*AnyApi* | [**get_asset**](docs/AnyApi.md#get_asset) | **GET** /assets/{name} | Displays the user dashboard page
*AnyApi* | [**refresh_token**](docs/AnyApi.md#refresh_token) | **POST** /token/refresh | Refreshes login token using refresh token
*DevelopersApi* | [**create_script**](docs/DevelopersApi.md#create_script) | **POST** /system/script | Create a new script
*DevelopersApi* | [**delete_script**](docs/DevelopersApi.md#delete_script) | **DELETE** /system/script | Delete a script
*DevelopersApi* | [**display_developer_dashboard**](docs/DevelopersApi.md#display_developer_dashboard) | **GET** /dashboard/developer | Displays the developer dashboard page
*DevelopersApi* | [**rename_script**](docs/DevelopersApi.md#rename_script) | **PATCH** /system/script | Rename a script
*DevelopersApi* | [**save_script**](docs/DevelopersApi.md#save_script) | **PUT** /system/script | Save a script
*UsersApi* | [**command**](docs/UsersApi.md#command) | **POST** /command | Execute a Command
*UsersApi* | [**display_dashboard**](docs/UsersApi.md#display_dashboard) | **GET** /dashboard | Displays the user dashboard page
*UsersApi* | [**endpoint_catalog**](docs/UsersApi.md#endpoint_catalog) | **GET** /system/endpoint/catalog | Retrieve the endpoint catalog
*UsersApi* | [**get_script**](docs/UsersApi.md#get_script) | **GET** /system/script | Retrieve the contents of a script
*UsersApi* | [**script_catalog**](docs/UsersApi.md#script_catalog) | **GET** /system/script/catalog | Retrieve the script catalog


## Documentation For Models

 - [AuthResponse](docs/AuthResponse.md)
 - [Command](docs/Command.md)
 - [Create](docs/Create.md)
 - [Delete](docs/Delete.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Execute](docs/Execute.md)
 - [Rename](docs/Rename.md)
 - [Response](docs/Response.md)
 - [Save](docs/Save.md)
 - [Script](docs/Script.md)
 - [UserAuth](docs/UserAuth.md)

## Author

shawn.clake@nopatience.net

