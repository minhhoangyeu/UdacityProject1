# Write-up Template
Title: "Hello World!"
Author: "Hoangnm22"
Body: "This is my first article!"
### Analyze, choose, and justify the appropriate resource option for deploying the app.

*For **both** a VM or App Service solution for the CMS app:*
- *Analyze costs, scalability, availability, and workflow*
- *Choose the appropriate solution (VM or App Service) for deploying the app*
- *Justify your choice*
- In this project I chose App service to deploy, this is a small project, so choosing an app service is the most appropriate. Because it is cheaper cost and faster setup compared with Vitural machine.
- The App Service:
  + Simplicity and Ease of Use
  + Typically more cost-effective, various pricing tiers including a free tier
  + Auto-scaling, built-in load balancing
  + Built-in security features, managed backups
- Virtual Machines (VMs):
   + Requires manual setup and management, full control over the OS
   + Potentially higher costs, pay-as-you-go based on VM size, storage, and network usage
   + Manual scaling, custom load balancing
   + Custom security configurations, manual backup setup and management
### Assess app changes that would change your decision.

*Detail how the app and any other needs would have to change for you to change your decision in the last section.* 

I would choose Virtual Machines if my project has complex dependencies or requires tool or application configuration that is resource-intensive and requires complex network configuration for specific security beyond features Managed security provided by Azure App Service.

But the current application service is more suitable for my project than Virtual Machine. Using Virtual Machines takes a lot of planning and work to keep them secure and up to date, so I don't see this changing in the near future if my projects don't grow larger and more complex.
