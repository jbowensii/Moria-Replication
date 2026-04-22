#!/usr/bin/env python3
"""
Build a truly minimal CPF_BearNest.umap — bare skeleton level with
no actors, no unused imports, minimal NameMap.
"""

import json
from pathlib import Path

src = Path(__file__).parent / 'CPF_BearNest.json'
dst = Path(__file__).parent / 'CPF_BearNest_minimal.json'

with open(src, 'r', encoding='utf-8') as f:
    data = json.load(f)

# ── Minimal NameMap: only names needed by Level, Model, World, WorldSettings ──
data['NameMap'] = [
    "/Game/Maps/Prefabs/CPF_BearNest",
    "/Script/CoreUObject",
    "/Script/Engine",
    "/Script/Moria",
    "Class",
    "CPF_BearNest",
    "Default__Level",
    "Default__Model",
    "Default__MorNavigationSystemConfig",
    "Default__World",
    "Default__WorldSettings",
    "Guid",
    "Level",
    "LevelBuildDataId",
    "Model",
    "MorNavigationSystemConfig",
    "MorNavigationSystemConfig_0",
    "NavigationSystemConfig",
    "None",
    "ObjectProperty",
    "Package",
    "PersistentLevel",
    "StructProperty",
    "World",
    "WorldSettings",
]

# ── Minimal Imports: only what Level/Model/World/WorldSettings/NavConfig need ──
data['Imports'] = [
    # -1: Level class
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "Level",
        "OuterIndex": -6,  # /Script/Engine
        "ClassPackage": "/Script/CoreUObject",
        "ClassName": "Class",
        "PackageName": None,
        "bImportOptional": False
    },
    # -2: Model class
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "Model",
        "OuterIndex": -6,  # /Script/Engine
        "ClassPackage": "/Script/CoreUObject",
        "ClassName": "Class",
        "PackageName": None,
        "bImportOptional": False
    },
    # -3: World class
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "World",
        "OuterIndex": -6,  # /Script/Engine
        "ClassPackage": "/Script/CoreUObject",
        "ClassName": "Class",
        "PackageName": None,
        "bImportOptional": False
    },
    # -4: WorldSettings class
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "WorldSettings",
        "OuterIndex": -6,  # /Script/Engine
        "ClassPackage": "/Script/CoreUObject",
        "ClassName": "Class",
        "PackageName": None,
        "bImportOptional": False
    },
    # -5: MorNavigationSystemConfig class
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "MorNavigationSystemConfig",
        "OuterIndex": -7,  # /Script/Moria
        "ClassPackage": "/Script/CoreUObject",
        "ClassName": "Class",
        "PackageName": None,
        "bImportOptional": False
    },
    # -6: /Script/Engine package
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "/Script/Engine",
        "OuterIndex": 0,
        "ClassPackage": "/Script/CoreUObject",
        "ClassName": "Package",
        "PackageName": None,
        "bImportOptional": False
    },
    # -7: /Script/Moria package
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "/Script/Moria",
        "OuterIndex": 0,
        "ClassPackage": "/Script/CoreUObject",
        "ClassName": "Package",
        "PackageName": None,
        "bImportOptional": False
    },
    # -8: Default__Level template
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "Default__Level",
        "OuterIndex": -6,
        "ClassPackage": "/Script/Engine",
        "ClassName": "Level",
        "PackageName": None,
        "bImportOptional": False
    },
    # -9: Default__Model template
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "Default__Model",
        "OuterIndex": -6,
        "ClassPackage": "/Script/Engine",
        "ClassName": "Model",
        "PackageName": None,
        "bImportOptional": False
    },
    # -10: Default__World template
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "Default__World",
        "OuterIndex": -6,
        "ClassPackage": "/Script/Engine",
        "ClassName": "World",
        "PackageName": None,
        "bImportOptional": False
    },
    # -11: Default__WorldSettings template
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "Default__WorldSettings",
        "OuterIndex": -6,
        "ClassPackage": "/Script/Engine",
        "ClassName": "WorldSettings",
        "PackageName": None,
        "bImportOptional": False
    },
    # -12: Default__MorNavigationSystemConfig template
    {
        "$type": "UAssetAPI.Import, UAssetAPI",
        "ObjectName": "Default__MorNavigationSystemConfig",
        "OuterIndex": -7,
        "ClassPackage": "/Script/Moria",
        "ClassName": "MorNavigationSystemConfig",
        "PackageName": None,
        "bImportOptional": False
    },
]

# ── Minimal Exports: PersistentLevel, Model, NavConfig, World, WorldSettings ──
# Export 1: PersistentLevel
export_level = {
    "$type": "UAssetAPI.ExportTypes.LevelExport, UAssetAPI",
    "Owner": None,
    "Actors": [5],  # WorldSettings only
    "URL": {
        "$type": "UAssetAPI.ExportTypes.FURL, UAssetAPI",
        "Protocol": "unreal",
        "Host": None,
        "Port": 7777,
        "Valid": 1,
        "Map": "/Game/Maps/Screens/SplashScreen",
        "Op": [],
        "Portal": None
    },
    "Model": 2,
    "ModelComponents": [],
    "LevelScriptActor": 0,
    "NavListStart": 0,
    "NavListEnd": 0,
    "Data": [
        {
            "$type": "UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI",
            "Name": "Model",
            "ArrayIndex": 0,
            "IsZero": False,
            "PropertyTagFlags": "None",
            "PropertyTagExtensions": "NoExtension",
            "Value": 2
        },
        {
            "$type": "UAssetAPI.PropertyTypes.Structs.StructPropertyData, UAssetAPI",
            "StructType": "Guid",
            "SerializeNone": True,
            "StructGUID": "{00000000-0000-0000-0000-000000000000}",
            "SerializationControl": "NoExtension",
            "Operation": "None",
            "Name": "LevelBuildDataId",
            "ArrayIndex": 0,
            "IsZero": False,
            "PropertyTagFlags": "None",
            "PropertyTagExtensions": "NoExtension",
            "Value": [
                {
                    "$type": "UAssetAPI.PropertyTypes.Structs.GuidPropertyData, UAssetAPI",
                    "Name": "LevelBuildDataId",
                    "ArrayIndex": 0,
                    "IsZero": False,
                    "PropertyTagFlags": "None",
                    "PropertyTagExtensions": "NoExtension",
                    "Value": "{CD5F78F2-4219-A9B4-6167-CFA37A8F6B65}"
                }
            ]
        },
        {
            "$type": "UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI",
            "Name": "WorldSettings",
            "ArrayIndex": 0,
            "IsZero": False,
            "PropertyTagFlags": "None",
            "PropertyTagExtensions": "NoExtension",
            "Value": 5
        }
    ],
    "ObjectGuid": None,
    "SerializationControl": "NoExtension",
    "Operation": "None",
    "ObjectName": "PersistentLevel",
    "OuterIndex": 4,       # outer = World (export 4)
    "ClassIndex": -1,      # Level class
    "SuperIndex": 0,
    "TemplateIndex": -8,   # Default__Level
    "ObjectFlags": "RF_Transactional",
    "SerialSize": 319,
    "SerialOffset": 0,
    "ScriptSerializationStartOffset": 0,
    "ScriptSerializationEndOffset": 0,
    "bForcedExport": False,
    "bNotForClient": False,
    "bNotForServer": False,
    "PackageGuid": "{00000000-0000-0000-0000-000000000000}",
    "IsInheritedInstance": False,
    "PackageFlags": "PKG_None",
    "bNotAlwaysLoadedForEditorGame": False,
    "bIsAsset": False,
    "GeneratePublicHash": False,
    "SerializationBeforeSerializationDependencies": [],
    "CreateBeforeSerializationDependencies": [5],
    "SerializationBeforeCreateDependencies": [-1, -8],
    "CreateBeforeCreateDependencies": [4],
    "Extras": "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=="
}

# Export 2: Model_0
export_model = {
    "$type": "UAssetAPI.ExportTypes.NormalExport, UAssetAPI",
    "Data": [],
    "ObjectGuid": None,
    "SerializationControl": "NoExtension",
    "Operation": "None",
    "ObjectName": "Model_0",
    "OuterIndex": 1,       # outer = PersistentLevel
    "ClassIndex": -2,      # Model class
    "SuperIndex": 0,
    "TemplateIndex": -9,   # Default__Model
    "ObjectFlags": "RF_Transactional",
    "SerialSize": 118,
    "SerialOffset": 0,
    "ScriptSerializationStartOffset": 0,
    "ScriptSerializationEndOffset": 0,
    "bForcedExport": False,
    "bNotForClient": False,
    "bNotForServer": False,
    "PackageGuid": "{00000000-0000-0000-0000-000000000000}",
    "IsInheritedInstance": False,
    "PackageFlags": "PKG_None",
    "bNotAlwaysLoadedForEditorGame": False,
    "bIsAsset": False,
    "GeneratePublicHash": False,
    "SerializationBeforeSerializationDependencies": [],
    "CreateBeforeSerializationDependencies": [],
    "SerializationBeforeCreateDependencies": [-2, -9],
    "CreateBeforeCreateDependencies": [1],
    "Extras": "AQAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAADAAAAAAAAAAMAAAAAAAAAEAAAAAAAAAAAAAAABgAAAAAAAAABAAAAAEAAAAAAAAAAAAAAAAAAAAX0wLbDkE6Rp0xJp6WF+JoAAAAAA=="
}

# Export 3: MorNavigationSystemConfig_0
export_navconfig = {
    "$type": "UAssetAPI.ExportTypes.NormalExport, UAssetAPI",
    "Data": [],
    "ObjectGuid": None,
    "SerializationControl": "NoExtension",
    "Operation": "None",
    "ObjectName": "MorNavigationSystemConfig_0",
    "OuterIndex": 5,       # outer = WorldSettings
    "ClassIndex": -5,      # MorNavigationSystemConfig class
    "SuperIndex": 0,
    "TemplateIndex": -12,  # Default__MorNavigationSystemConfig
    "ObjectFlags": "RF_NoFlags",
    "SerialSize": 12,
    "SerialOffset": 0,
    "ScriptSerializationStartOffset": 0,
    "ScriptSerializationEndOffset": 0,
    "bForcedExport": False,
    "bNotForClient": False,
    "bNotForServer": False,
    "PackageGuid": "{00000000-0000-0000-0000-000000000000}",
    "IsInheritedInstance": False,
    "PackageFlags": "PKG_None",
    "bNotAlwaysLoadedForEditorGame": False,
    "bIsAsset": False,
    "GeneratePublicHash": False,
    "SerializationBeforeSerializationDependencies": [],
    "CreateBeforeSerializationDependencies": [],
    "SerializationBeforeCreateDependencies": [-5, -12],
    "CreateBeforeCreateDependencies": [5],
    "Extras": ""
}

# Export 4: CPF_BearNest (World)
export_world = {
    "$type": "UAssetAPI.ExportTypes.NormalExport, UAssetAPI",
    "Data": [],
    "ObjectGuid": None,
    "SerializationControl": "NoExtension",
    "Operation": "None",
    "ObjectName": "CPF_BearNest",
    "OuterIndex": 0,
    "ClassIndex": -3,      # World class
    "SuperIndex": 0,
    "TemplateIndex": -10,  # Default__World
    "ObjectFlags": "RF_Public, RF_Standalone, RF_Transactional",
    "SerialSize": 24,
    "SerialOffset": 0,
    "ScriptSerializationStartOffset": 0,
    "ScriptSerializationEndOffset": 0,
    "bForcedExport": False,
    "bNotForClient": False,
    "bNotForServer": False,
    "PackageGuid": "{00000000-0000-0000-0000-000000000000}",
    "IsInheritedInstance": False,
    "PackageFlags": "PKG_None",
    "bNotAlwaysLoadedForEditorGame": False,
    "bIsAsset": True,
    "GeneratePublicHash": False,
    "SerializationBeforeSerializationDependencies": [],
    "CreateBeforeSerializationDependencies": [],
    "SerializationBeforeCreateDependencies": [-3, -10],
    "CreateBeforeCreateDependencies": [],
    "Extras": "BAAAAAAAAAAAAAAA"
}

# Export 5: WorldSettings
export_worldsettings = {
    "$type": "UAssetAPI.ExportTypes.NormalExport, UAssetAPI",
    "Data": [
        {
            "$type": "UAssetAPI.PropertyTypes.Objects.ObjectPropertyData, UAssetAPI",
            "Name": "NavigationSystemConfig",
            "ArrayIndex": 0,
            "IsZero": False,
            "PropertyTagFlags": "None",
            "PropertyTagExtensions": "NoExtension",
            "Value": 3  # NavConfig export
        }
    ],
    "ObjectGuid": None,
    "SerializationControl": "NoExtension",
    "Operation": "None",
    "ObjectName": "WorldSettings",
    "OuterIndex": 1,       # outer = PersistentLevel
    "ClassIndex": -4,      # WorldSettings class
    "SuperIndex": 0,
    "TemplateIndex": -11,  # Default__WorldSettings
    "ObjectFlags": "RF_Transactional",
    "SerialSize": 118,
    "SerialOffset": 0,
    "ScriptSerializationStartOffset": 0,
    "ScriptSerializationEndOffset": 0,
    "bForcedExport": False,
    "bNotForClient": False,
    "bNotForServer": False,
    "PackageGuid": "{00000000-0000-0000-0000-000000000000}",
    "IsInheritedInstance": False,
    "PackageFlags": "PKG_None",
    "bNotAlwaysLoadedForEditorGame": False,
    "bIsAsset": False,
    "GeneratePublicHash": False,
    "SerializationBeforeSerializationDependencies": [3],
    "CreateBeforeSerializationDependencies": [],
    "SerializationBeforeCreateDependencies": [-4, -11],
    "CreateBeforeCreateDependencies": [1],
    "Extras": ""
}

data['Exports'] = [
    export_level,
    export_model,
    export_navconfig,
    export_world,
    export_worldsettings,
]

# ── Clean up metadata ──
data['DependsMap'] = [[], [], [], [], []]
data['Generations'] = [{
    "$type": "UAssetAPI.FGenerationInfo, UAssetAPI",
    "ExportCount": 5,
    "NameCount": len(data['NameMap'])
}]
data['SoftObjectPathList'] = None
data['SearchableNames'] = None
data['Thumbnails'] = None
data['WorldTileInfo'] = None
data['SoftPackageReferenceList'] = None
data['NamesReferencedFromExportDataCount'] = len(data['NameMap'])

# Remove custom versions that reference bear/unused systems
# Keep only core ones needed for basic level
data['CustomVersionContainer'] = [
    cv for cv in data['CustomVersionContainer']
    if cv['FriendlyName'] in (
        'FCoreObjectVersion',
        'FEditorObjectVersion',
        'FFrameworkObjectVersion',
        'FReleaseObjectVersion',
    )
]

print(f"Exports: {len(data['Exports'])}")
print(f"Imports: {len(data['Imports'])}")
print(f"NameMap: {len(data['NameMap'])}")
print(f"CustomVersions: {len(data['CustomVersionContainer'])}")
for i, exp in enumerate(data['Exports']):
    print(f"  Export {i+1}: {exp['ObjectName']}")
for i, imp in enumerate(data['Imports']):
    print(f"  Import -{i+1}: {imp['ObjectName']}")

with open(dst, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2)

print(f"\nWrote: {dst}")
