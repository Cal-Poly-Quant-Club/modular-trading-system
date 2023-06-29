# hft-system
# Project Description
Building a High-Frequency Trading (HFT) System using Python

# Project Work
All project work will be compiled in this Github Repo

# Project Members:
Charlie Ray

Noor Dhaliwal

# Overview
This project's objective is to create a Python-based High-Frequency Trading (HFT) system that integrates real-time data and a statistical model to make informed trades. The system should leverage the "cpquant" library and be designed in a modular way, allowing for easy swapping of statistical models like building blocks. The final deliverable is technical documentation explaining the system's inner workings and architecture, which is distinct from the user-facing "cpquant" library documentation.

# Objectives
Design and implement an HFT system capable of receiving and processing real-time data.

Enable the HFT system to apply statistical models to inform trading decisions.

Integrate the "cpquant" library into the HFT system for data handling and quantitative analysis.

Construct the system in a modular fashion to allow statistical models to be easily swapped.

Write detailed technical documentation explaining how the system operates, its architecture, and how to incorporate and swap statistical models.

# Deliverables
A Python-based HFT system that uses real-time data and statistical models to make trading decisions.

Comprehensive technical documentation describing the system's functionality and architecture.

# Methodology
The project should commence with a deep understanding of HFT systems and the requirements of handling real-time data. Once the foundation is laid, the system can be designed to incorporate statistical models and to utilize the "cpquant" library for data handling. The system should be modular, allowing statistical models to be easily added or removed. Throughout the process, the team should document the technical aspects of the system, leading to a comprehensive technical documentation.

# Timeline
Weeks 1-2: Research and understand the requirements and architecture of HFT systems.

Weeks 3-4: Design the initial structure of the HFT system.

Weeks 5-6: Incorporate the "cpquant" library into the HFT system and ensure it can handle real-time data.

Weeks 7-8: Implement the functionality to add and swap statistical models.

Weeks 9-10: Draft, review, and finalize the technical documentation.

# Roles and Responsibilities
The team can be divided into roles such as System Architects, Real-Time Data Specialists, Model Integration Developers, and Technical Writers.

# Resources
[High-Frequency Trading Systems and Networks](https://towardsdatascience.com/assembling-an-entry-level-high-frequency-trading-hft-system-e7538545b2a9)

[Real-Time Data Processing](https://corporatefinanceinstitute.com/resources/data-science/time-series-data-analysis/)

[Unix systemctl](https://www.digitalocean.com/community/tutorials/how-to-use-systemctl-to-manage-systemd-services-and-units)

[Sockets](https://www.developer.com/web-services/intro-web-sockets/)

# Evaluation Criteria
You should evaluate this project based on the following:

The ability of the system to process real-time data accurately and efficiently.

The system's successful integration with the "cpquant" library.

The flexibility of the system in adding and swapping statistical models.

The comprehensiveness, accuracy, and clarity of the technical documentation.

# Communication and Collaboration
Regular team meetings should be scheduled to discuss progress, troubleshoot issues, and exchange ideas. Active collaboration and open communication are key to the project's success.

# Creativity and Learning
The team is encouraged to use their creativity and learning to develop an efficient and flexible HFT system. Although the main objectives are clear, there is room for innovation and improvement at every step. Your insights and expertise will be instrumental in shaping a successful HFT system.

# Additional Notes
The “Sockets” resource is mostly to familiarize you with what sockets are; ideally, all socket handling is provided by the cpquant library. For a rough overview, you will create a systemctl service that runs a python program, the python program will then connect to a realtime data socket provided by the cpquant library, from there you will interface with the statistical model (for this project, use a really simple one, ex if volume % 17 == 0, sell 5 shares SPY, else if volume % 31 == 0, buy 5 shares SPY, there is no rational to this statistical model, other than it’s simple and uses a little bit of the realtime data), when you get one of the buy/sell signals, interface again with the cpquant library to place the actual paper trades on the account. Make sure to turn yourself off when markets are closed (holiday, outside of market hours, ect)


