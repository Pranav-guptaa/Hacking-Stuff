## Try Hack Me ---> Splunk(Helps in Detecting Attacks)
# Crendiatials

Username: splunkadmin

Password: AdminAdmin01

# Splunk PDF
```Events: 
An event is a set of values associated with a timestamp. 
It is a single entry of data and can have one or multiple lines.
An event can be a text document, a configuration file, an entire
stack trace, and so on.

this is an example of an
event in a web activity log:
173.26.34.223 - - [01/Mar/2015:12:05:27 -0700] “GET /trade/app?action=logout HTTP/1.1”200 2953      
```

```Metrics

A metric consists of a timestamp, metric
name, measure and dimensions.
A measure is a numeric data point while dimensions help
categorize these data points. 
Sample metric: 

Timestamp: 01/Aug/2017 12:05:27
Metric Name: os.cpu.user
Measure: 42.12345
Dimensions: hq:us-west-1, hq:us-east-1 

Metrics and Events can be searched and
correlated together but are stored in different
indexes.
```

```(Hosts, Source and Source Types)

Hosts: 	A host is the name of the physical or virtual device where an event 				originates. 
		It can be used to find all data originating from a specific device.

Source: A source is the name of the file, directory, data
		stream, or other input from which a particular
		event originates. 

Source 
Types:	Sources are classified into source types, which can be either well 	known
		formats or formats defined by the user. Some
		common source types are HTTP web server logs
		and Windows event logs.
		Events with the same source types can come from
		different sources. For example, events from the
		file source=/var/log/messages and from a
		syslog input port source=UDP:514 often share
		the source type, sourcetype=linux _ syslog.
```


## Qustions on thm(Splunk)

1. Splunk queries always begin with this command implicitly unless otherwise specified. What command is this? When performing additional queries to refine received data this command must be added at the start. This is a prime example of a slight trick question.
Answer: search

2. When searching for values, it's fairly typical within security to look for uncommon events. What command can we include within our search to find these?
Answer: 
