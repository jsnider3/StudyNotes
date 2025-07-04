# Becoming a Cloud Practicioner
Instructor is Curtis Nelson.
## 2023/10/03 Part 1 - https://www.aws.training/Details/InstructorLedTraining?id=136736
This is intended to prepare for the AWS Certification. There will be multiple choice
questions that are similar to the questions on the certification exam, which you should
try to take within a few months. There are beta questions in the exam that aren't counted.

### Intro
Gave the outline for the entire series.
Materials for this class will be sent out by email. It will just be slides and slide notes.
AWS has over 250 services.

#### Understanding networks

Traditional way is the client-server model.
PC -> router -> ISP -> Internet

On-premises compute gives you a great deal of headaches, but also a great deal of control.
Cloud lets you pass all of the hardware responsibility onto the cloud.
Hybrid is where you share the responsibility.

Three main models (Most to least on-prem): 
* Infrastructure-as-a-Service - Amazon Web Services
* Platform-as-a-Service - AWS Elastic Beanstalk, SAP Cloud
* Software-as-a-Service - Dropbox, Slack, Salesforce

#### Cloud computing benefits
* Replace upfront expenses with variable and over-time costs.
* Can shift focus to applications and customers and away from running data centers.
* Capacity can scale up and down as needed instead of needing you to guess well.
* Benefit from the economies of scale from other customers.
* Deploy globally in minutes.

What is cloud computing?
* Using on-demand delivery of IT resources and applications through the Internet.

### Global Infrastructure and Reliability
Amazon has 102 availability zones in 32 regions.
Amazon sometimes loses data centers, occasionally loses availability zones, but never loses regions.

AWS has a long list of services which we went over.

### Networking

Terminology in this module: Data packets, protocol, port/port number,
Topic A: Amazon Virtual Private Cloud (Amazon VPC)

o Interactive Demo 1: Building a VPC

The number after the slash in a VPC says how many bits identify the network.

We can create subnets, some of which are public and some of which are private.

A route table is the set of rules that determine where network traffic is directed.


Topic B: Network access control lists and security groups

o Interactive Demo 2: Viewing Internet Gateways and route tables

o Interactive Demo 3: Viewing ACLs and SGs

Which of the following describes how you would create a public subnet?
* Create a subnet. Create a route in the subnet's route table with the target of the internet gateway.

Your company needs a high speed dedicated connection to the AWS Cloud. Which should you recommend?
* Direct connect

### Object Storage
Distinct from block and file. Amazon's solution is called S3.
An object consists of data, metadata, and a key.
Buckets must have universally unique names.

S3 storage classes
* Standard: Frequently accessed data, stored in 3+ availability zones
* Standard-IA: Ideal for infrequently accessed data. Cheaper to store, but harder to retrieve.
* One Zone-IA: Stores in a single availability zone, cheaper than Standard-IA.
* Intelligent-tiering: Moves stuff around to best tier.
* Glacier: Cheap, with a few minutes/hours of latency
* Glacier Deep Archive: Cheapest with ~12 hours of latency.

Amazon can automatically age things to different classes.

Amazon S3 pricing is based on four factors: Storage, requests and data retrievals, data transfer, management/replication

AWS Snow Family
* AWS Snowcone - Small, regular data transfer device, 8 TB.
* AWS Snowball - Rack-mountable, but 80 TB or so.
* AWS Snowmobile - Shipping container sized device, pulled by tractor trailer. Up to 100 PB.

Which S3 classes are optimized for archiver data?
* Glacier and Glacier Deep Archive

## Part 2

### Security

### Block and File Storage

### Compute in the Cloud

## Part 3

### AWS Frameworks, Pricing, Support

### Applications in the Cloud

### Databases

### Monitoring and Analytics

## Exam prep
Teacher is Chris Woolief, Senior Technical Instructor, woodliec@amazon.com.

This is an exam prep class, not one to actually teach you about stuff.

He has a husky dog called Kylo.

Should be receiving the course slides later today.

### Domain 1
https://aws.amazon.com/certification/certified-cloud-practitioner/
25% off coupon at https://pages.awscloud.com/GLOBAL-ln-GC-Cloud-Practitioner-Certification-Challenge-2023-reg.html?trk=0213f737-9401-4a91-9d64-c2427240fef6&sc_channel=el

He recommends being very familiar with the shared responsibility model. "If you can configure it, you are responsible for it."

Be able to go through the list of In-scope Amazon services and say a sentence or two. The exam is like a vocabulary exam.

The exam is the same content as the previous version, but with different weighting.

In order to pass, you must get 700 points out of 1000. This is not exactly the same as getting 70%, but close enough.

AWS Reinvent is a big event coming up soon.

The three classes contain most of the info needed for the tests, but not all of it. Check the exam guide.

Questions on practicioner tend to be short, professional tends to be longer.

Total cost of ownership costs.

Design for failure.