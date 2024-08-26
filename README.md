# Course Registration and Curricular Data Analysis

This project demonstrates a comprehensive data analysis pipeline designed to extract, transform, and analyze course registration and curricular data for the ADS (Applied Data Science) and IS (Information Systems) programs. The aim is to uncover valuable insights and patterns from the student enrollment system data, leveraging distributed data processing tools and techniques.

## Table of Contents

1. [Introduction](#introduction)
2. [Objectives](#objectives)
3. [Data Sources](#data-sources)
4. [Technologies and Tools](#technologies-and-tools)
5. [Project Setup](#project-setup)
6. [Data Processing Workflow](#data-processing-workflow)
7. [Results and Insights](#results-and-insights)
8. [Challenges and Learnings](#challenges-and-learnings)
9. [Conclusion](#conclusion)
10. [License](#license)
11. [Acknowledgments](#acknowledgments)

## Introduction

This project involves analyzing course registration and student enrollment data to provide actionable insights for curriculum development and student performance evaluation. The analysis covers data integration, preparation, querying, and visualization, all conducted in a distributed computing environment.

## Objectives

The primary objectives of this project are:

- To integrate and process data from multiple sources, including MongoDB, Minio, Cassandra, Elasticsearch, and Neo4j.
- To perform data analysis to identify trends in course enrollment, student performance, and program effectiveness.
- To create visualizations and dashboards that aid in decision-making for academic planning and resource allocation.

## Data Sources

The project utilizes various datasets provided by the iSchool, including:

- **MongoDB**: Contains reference data for courses, terms, programs, and students.
- **Minio**: Stores raw student enrollment data in CSV format (`sections.csv` and `enrollments.csv`).
- **Cassandra and Elasticsearch**: Used for storing and querying processed data.
- **Neo4j**: Used for representing and analyzing relationships between courses and programs.

## Technologies and Tools

The following technologies and tools were utilized in this project:

- **Apache Spark**: For distributed data processing and complex transformations.
- **Docker**: To create a consistent environment for running multiple services simultaneously.
- **MongoDB, Minio, Cassandra, Elasticsearch, Neo4j**: For storing, managing, and querying data.
- **Kibana**: For creating dynamic dashboards and visualizations.
- **Python**: For scripting and automation.
- **Jupyter Notebooks**: For developing and testing data processing workflows interactively.

## Project Setup

### Prerequisites

To set up this project, ensure you have the following:

- Docker and Docker Compose installed.
- Python environment with Jupyter Notebook support.
- Basic understanding of distributed data processing and database management.

### Installation and Setup

1. **Clone the Repository**

    ```bash
    git clone https://github.com/yourusername/course-data-analysis.git
    cd course-data-analysis
    ```

2. **Build and Start Docker Containers**

    Build the necessary Docker containers and start the environment:

    ```bash
    docker-compose build
    docker-compose up -d
    ```

3. **Verify Environment Setup**

    Ensure all services (MongoDB, Minio, Cassandra, Elasticsearch, Neo4j) are running properly:

    ```bash
    docker-compose ps
    ```

4. **Load Initial Data**

    Check the data loader service logs to ensure all data is imported correctly:

    ```bash
    docker-compose logs dataloader
    ```

    Look for the message: `DONE! dataloader is complete!`

## Data Processing Workflow

The project follows a structured data processing workflow to ensure comprehensive analysis:

1. **Data Ingestion**: Read data from various sources using PySpark, including raw enrollment and section data from Minio, and reference data from MongoDB.
   
2. **Data Preparation**: Clean and transform the data, preparing it for loading into Cassandra and Elasticsearch. The preparation involves flattening nested structures and ensuring data compatibility.

3. **Data Analysis and Queries**: Utilize PySpark and Spark SQL to perform complex data queries. This includes analyzing course enrollment trends, student performance metrics, and identifying popular and challenging courses.

4. **Graph Data Modeling**: Load courses and program data into Neo4j to model relationships such as prerequisites and elective requirements. Analyze these relationships to understand the program structure better.

5. **Visualization and Dashboard Creation**: Use Kibana to build interactive dashboards, providing visual insights into student enrollments, course capacities, program completions, and other key metrics.

## Results and Insights

### Key Findings

- **Enrollment Trends**: Analysis revealed the most popular courses and those with the highest dropout rates, providing insight into student preferences and potential areas for curriculum improvement.
  
- **Student Performance**: Identified top-performing students and courses with the highest success rates, enabling targeted academic support and recognition programs.

- **Program Effectiveness**: Assessed the effectiveness of the ADS and IS programs based on student outcomes and course feedback, suggesting adjustments to course offerings and prerequisites.

### Example Outputs

- **Interactive Dashboards**: Created in Kibana to visualize real-time enrollment data, course capacities, and student performance metrics.
- **Neo4j Graph Visualizations**: Displayed relationships between courses, prerequisites, and electives, providing a clear view of curriculum dependencies.
- **Processed DataFrames**: Prepared and loaded wide tables into Cassandra and Elasticsearch for efficient querying and analysis.

## Challenges and Learnings

### Challenges

- **Data Integration Complexity**: Integrating data from multiple, disparate sources required careful planning and validation to ensure consistency and reliability.
- **Performance Optimization**: Optimizing PySpark queries and transformations to handle large datasets efficiently within a distributed environment posed significant challenges.
- **Visualizing Complex Data**: Creating meaningful visualizations from complex, multi-dimensional data required a deep understanding of both the data and the tools.

### Learnings

- Gained expertise in handling distributed databases and data integration challenges.
- Developed advanced skills in data transformation, preparation, and querying using PySpark and Spark SQL.
- Enhanced ability to create interactive and insightful visualizations using Kibana and Neo4j.

## Conclusion

The Course Registration and Curricular Data Analysis project successfully demonstrates the ability to integrate, process, and analyze data in a distributed environment. The insights derived from this analysis provide valuable input for academic planning and resource allocation, contributing to the improvement of educational programs.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

