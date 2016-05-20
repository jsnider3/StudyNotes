# Azure

Free Trial comes with $200 of credit.

Hadoop is provided as Azure HDInsight.

VS Code is an IDE, it's very different from Visual Studio
despite the similar names.

There's a node package called azure-cli, which is useful to
manage azure projects from the command line.

I had some slight confusion when setting up azure-cli as to which
account I had associated with my free trial.

## Bug Log

* Later I had some difficulty creating an Azure project in Visual Studio.
  When I tried logging in to Azure, it would say that it couldn't log me in
  and that I should contact customer service. It turns out that my free trial
  had expired at that point and was being weird about it. I just signed up for
  the paid version and the issue went away.

## Kerbalize

I have an idea for an Azure app. A translator that takes text from any language
and converts it to Kerbal audio. Since we know that Kerbal is actually Spanish played
in reverse, we can accomplish this through three steps:
1) Convert the text to Spanish.
2) Convert the Spanish to audio.
3) Reverse the audio and give the user a link to download that file.

It looks like both steps one and two can be done with Microsoft Translator.
Step three will probably be tricky even though there is no reason for it to be.

Once the system is working I should consider using Azure Blob store to save time.
I can see arguments that caching both will and won't be an improvement.