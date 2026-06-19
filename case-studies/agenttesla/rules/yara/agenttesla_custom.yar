rule AgentTesla_Combined_Static_IOC
{
    meta:
        description = "Defensive detection for AgentTesla-related static traits from the completed investigation"
        author = "James Banday"
        incident_id = "INC2026-0203-AGENTTESLA"
        malware_family = "AgentTesla"
        sha256 = "bc37921377b4fe391a8487b7116cb8b92b3b09b1c0e9b4f48fb99f217f43eec2"
        version = "1.0"
        scope = "Defensive lab validation only; no malware sample is included in this repository"

    strings:
        $s1 = "Unre.exe" fullword ascii wide
        $s2 = "MothGarden" fullword ascii wide
        $s3 = "MothGarden.Properties" ascii wide
        $s4 = "MothGarden.Properties.Resources.resources" ascii wide

    condition:
        uint16(0) == 0x5A4D and
        filesize < 1200KB and
        2 of ($s*)
}
