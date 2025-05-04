# Cuna

**Cuna** is an AI-powered tool that transforms natural language descriptions into fully functional network topologies. Designed for cybersecurity professionals, network engineers, educators, and students, Cuna bridges the gap between human intention and technical implementation—instantly generating topologies compatible with tools like **GNS3**, **Cisco Packet Tracer**, and other network simulation environments.

## 🚀 Features

- 🧠 **Natural Language Input**  
  Describe your desired network in plain English—Cuna interprets and builds it.

- 🗺️ **Auto-Generated Topologies**  
  Output valid topology files (e.g., `.net`, `.gns3`, `.pkt`, or YAML/JSON) from prompts.

- 🧩 **Device & Protocol Support**  
  Support for routers, switches, firewalls, subnets, VLANs, VPNs, and more.

- 🔁 **Editable Output**  
  Review and tweak generated files before importing into your network simulator.

- 🧪 **Built with extensibility in mind**  
  Modular design makes it easy to integrate with other automation tools and pipelines.

## 🧑‍💻 Example Usage

```plaintext
Prompt:
"Create a network with two routers connected to each other. Each router connects to two PCs. Use OSPF as the routing protocol."

Output:
A topology file compatible with GNS3 or Packet Tracer, complete with device configuration.
