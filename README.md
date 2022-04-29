<div align="center">
  <a href="https://github.com/ScobioalaMaria/H-Elite">
    <img src="H-Elite-logo.png" alt="Logo" width="300" height="300">
  </a>
<h3 align="center">H-Elite</h3>

  <p align="center">
    Lab of software development project
  </p>
</div>

<details open>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#tests">Tests</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
The aim is to develop a project where users can save a series of information related to an artist. 
<p align="right">(<a href="#top">Back to top</a>)</p>


<!-- GETTING STARTED -->
## Getting Started

These are the instructions to run our project locally on your machine.

### Prerequisites

List of things you need to use the software and how to install them.
We used a module called prettytable please install it before trying to run our program. 

  ```sh
  python3 -m pip install prettytable
  ```

### Installation

You can then run the file main.py using python

 ```py
  python3 main.py
  ```
<p align="right">(<a href="#top">Back to top</a>)</p>

<!--USAGE -->
## Usage

The aim of this project is the development of a software where you can save data about your favourite artsist, we have already added some arstists.

In order to run the program, to understand the commands you should start from here:

  ```sh
  python3 main.py -h
  ```
  or 
  ```sh
  python3 main.py --help
  ```

We have five functions that can be runned by the program, that are called:
<br>
  ```sh
  -v or --view
  ```
  The output will present a tabled view of all the artists saved in the file. 
  <br>
  ```sh
  -a or --add
  ```
  You can add an artist and the output will show you the artist added.
 <br>
  ```sh
  -s or --search
  ```
  You can search for a specific artist by inputting its name or surname. 
  The output will present a tabled view with the search results. 
  <br>
  ```sh
  -m or --movement
  ```
  You can search for artist that have the same movement.   
  The output will present a tabled view with the search results. 
<br>
  ```sh
  -c or --compare
  ```
You can search for artists that have the same nationality and movement.   
The output will present a tabled view with the search results. 

<br>


To run the functions add the arguments specified above
This is an example:
  ```sh
  python3 main.py -v
  ```

<p align="right">(<a href="#top">Back to top</a>)</p>

<!-- TESTS -->
## Tests

The project has been tested with the unittest suite that you can find in the folder tests.
Tests regarding the input taken have not been conducted as the program does not run if you don't give the arguments to the argparse 
<br>
To run the test suite do the following:
  ```sh
  python3 -m unittest tests/test_functions.py
  ```

<p align="right">(<a href="#top">Back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the GNU General Public License v3.0. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">Back to top</a>)</p>

<!-- CONTACT -->
## Contact

Corinne Mohideen Murgueitio - corinne.mohideenmurgueitio@student.h-farm.com
<br />
Massimo Sirianni - massimo.sirianni@student.h-farm.com
<br />
Maria Scobioala  - maria.scobioala@student.h-farm.com 
<br />
Project Link: [https://github.com/ScobioalaMaria/H-Elite](https://github.com/ScobioalaMaria/H-Elite)

<p align="right">(<a href="#top">Back to top</a>)</p>
